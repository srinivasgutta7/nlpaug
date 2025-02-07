import random
import numpy as np
from multiprocessing.dummy import Pool as ThreadPool

from nlpaug.util import Action, Method, WarningException, WarningName, WarningCode, WarningMessage


class Augmenter:
    def __init__(self, name, method, action, aug_min, aug_max, aug_p=0.1, device='cpu', verbose=0):
        self.name = name
        self.action = action
        self.method = method
        self.aug_min = aug_min
        self.aug_max = aug_max
        self.aug_p = aug_p
        self.device = device
        self.verbose = verbose

        # if seed is not None:
        #     random.seed(seed)
        #     np.random.seed(seed)
        #     torch.manual_seed(seed)
        #     torch.cuda.manual_seed(seed)

        self.augments = []

        self._validate_augmenter(method, action)

    @classmethod
    def _validate_augmenter(cls, method, action):
        if method not in Method.getall():
            raise ValueError(
                'Method must be one of {} while {} is passed'.format(Method.getall(), method))

        if action not in Action.getall():
            raise ValueError(
                'Action must be one of {} while {} is passed'.format(Action.getall(), action))

    def augment(self, data, n=1, num_thread=1):
        """
        :param object data: Data for augmentation
        :param int n: Number of unique augmented output
        :param int num_thread: Number of thread for data augmentation. Use this option when you are using CPU and
            n is larger than 1
        :return: Augmented data

        >>> augmented_data = aug.augment(data)

        """
        max_retry_times = 3  # max loop times of n to generate expected number of outputs

        exceptions = self._validate_augment(data)
        # TODO: Handle multiple exceptions
        for exception in exceptions:
            if isinstance(exception, WarningException):
                if self.verbose > 0:
                    exception.output()

                # Return empty value per data type
                if isinstance(data, str):
                    return ''
                elif isinstance(data, list):
                    return []
                elif isinstance(data, np.ndarray):
                    return np.array([])

                return None

        results = []
        action_fx = None
        clean_data = self.clean(data)
        if self.action == Action.INSERT:
            action_fx = self.insert
        elif self.action == Action.SUBSTITUTE:
            action_fx = self.substitute
        elif self.action == Action.SWAP:
            action_fx = self.swap
        elif self.action == Action.DELETE:
            action_fx = self.delete
        elif self.action == Action.SPLIT:
            action_fx = self.split

        for _ in range(max_retry_times+1):
            augmented_results = []
            if num_thread == 1:
                augmented_results = [action_fx(clean_data) for _ in range(n)]
            else:
                if self.device == 'cpu':
                    augmented_results = self._parallel_augment(action_fx, clean_data, n=n, num_thread=num_thread)
                elif self.device == 'cuda':
                    # TODO: support multiprocessing for GPU
                    # https://discuss.pytorch.org/t/using-cuda-multiprocessing-with-single-gpu/7300
                    augmented_results = [action_fx(clean_data) for _ in range(n)]
                else:
                    raise ValueError('Unsupported device mode [{}]. Only support `cpu` or `cuda`'.format(self.device))

            for augmented_result in augmented_results:
                if not self.is_duplicate(results + [data], augmented_result):
                    results.append(augmented_result)

                if len(results) >= n:
                    break
            if len(results) >= n:
                break

        # TODO: standardize output to list even though n=1 from 1.0.0
        if len(results) == 0:
            # if not result, return itself
            if n == 1:
                return data
            else:
                return [data]
        if n == 1:
            return results[0]
        return results[:n]

    @classmethod
    def _validate_augment(cls, data):
        if data is None or len(data) == 0:
            return [WarningException(name=WarningName.INPUT_VALIDATION_WARNING,
                                     code=WarningCode.WARNING_CODE_001, msg=WarningMessage.LENGTH_IS_ZERO)]

        return []

    @classmethod
    def _parallel_augment(cls, action_fx, data, n, num_thread=2):
        pool = ThreadPool(num_thread)
        results = pool.map(action_fx, [data] * n)
        pool.close()
        pool.join()
        return results

    def insert(self, data):
        raise NotImplementedError

    def substitute(self, data):
        raise NotImplementedError

    def swap(self, data):
        raise NotImplementedError

    def delete(self, data):
        raise NotImplementedError

    def split(self, data):
        raise NotImplementedError

    def tokenizer(self, tokens):
        raise NotImplementedError

    def evaluate(self):
        raise NotImplementedError

    @classmethod
    def is_duplicate(cls, dataset, data):
        raise NotImplementedError

    @classmethod
    def prob(cls):
        return random.random()

    @classmethod
    def sample(cls, x, num):
        if isinstance(x, list):
            return random.sample(x, num)
        elif isinstance(x, int):
            return random.randint(1, x-1)

    @classmethod
    def clean(cls, data):
        raise NotImplementedError

    def _generate_aug_cnt(self, size, aug_min, aug_max, aug_p=None):
        if aug_p is not None:
            percent = aug_p
        elif self.aug_p is not None:
            percent = self.aug_p
        else:
            percent = 0.3
        cnt = int(percent * size)

        if cnt < aug_min:
            return aug_min
        if aug_max is not None and cnt > aug_max:
            return aug_max
        return cnt

    def generate_aug_cnt(self, size, aug_p=None):
        return self._generate_aug_cnt(size, self.aug_min, self.aug_max, aug_p)

    def generate_aug_idxes(self, inputs):
        aug_cnt = self.generate_aug_cnt(len(inputs))
        token_idxes = [i for i, _ in enumerate(inputs)]
        aug_idxes = self.sample(token_idxes, aug_cnt)
        return aug_idxes

    def __str__(self):
        return 'Name:{}, Action:{}, Method:{}'.format(self.name, self.action, self.method)
