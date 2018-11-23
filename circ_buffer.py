# -*- coding: utf-8 -*-
"""
This is Circular Buffer module
2018.23.01- support for any kind of data: lists, objects, dicts and so on
"""
# Exceptions


class CircBufferError(Exception):
    """
    exception definition
    """
    pass


class InputTooBig(CircBufferError):
    """
    exception definition
    """
    pass


class ArgLenGreaterThan1(Exception):
    """
    """
    pass

class NotIntegerBufferSizeProvided(CircBufferError):
    """
    exception definition
    """
    pass


class NotValidBufferSizeProvided(CircBufferError):
    """
    exception definition
    """
    pass


class GetsMethodCalledForNonStrType(CircBufferError):
    """
    exception definition
    """
    pass


class Cbuffer(object):
    """
    Circular buffer
    """
    def __init__(self, b_size=100, init_buffer=None):
        self._head = 0
        self._tail = 0
        self._index = 0
        self.size = b_size
        self.buffer = b_size*['']
        self._available = 0
        self.copy_init_vals_if_provided(init_buffer)

    def available(self):
        return self._available

    def __add__(self, string):
        """Support of + and += operator"""
        for elem in string:
            self.put(elem)
        return self

    def copy_init_vals_if_provided(self, _buffer):
        """
        Will copy buffer to self.buffer
        :param _buffer:
        :return:
        """
        if _buffer:
            for elem in _buffer:
                self.put(elem)

    def flush(self):
        """
        flush circ buffer
        :return:
        """
        self._head = 0
        self._tail = 0
        self.size = self.size
        # TODO: you can remove below line so __contains__ operator will work
        # but you have to overload __contains__
        # It must check only "available" amount of data starting from head to
        # tail, or easier: after flush it should be:
        # cbuffer.flush()
        # if "string" in buffer -> __contains__: if available and string in
        # self.buffer[self._tail:available]
        self.buffer = self.size*['']
        self._available = 0

    def put(self, char):
        """
        puts new element
        :param char:
        :return:
        """
        if len(char) > 1:
            raise ArgLenGreaterThan1
        self.buffer[self._tail] = char
        self._tail = (self._tail + 1) % self.size
        if self._available < self.size:
            self._available += 1
        if self._available == self.size:
            self._head = self._tail

    def get(self):
        """
        gets oldest element
        :return:
        """
        if self._available:
            self._available -= 1
            tmp_char = self.buffer[self._head]
            self._head = (self._head + 1) % self.size
            return tmp_char
        else:
            return None

    def _get_as_list(self):
        return [self.get()]

    def gets(self, amount=None):
        """
        gets given amount of oldest elements or all available elements
        if amount not provided
        :param amount:
        :return:
        """

        if not self._available:
            return None
        if not amount:
            amount = self._available
        tmp_buff = self.get()
        amount -= 1
        # get_method = self.get
        # if not isinstance(tmp_buff, str):
        #     get_method = self._get_as_list
        #     tmp_buff = [tmp_buff]
        while (amount) and self._available:
            # tmp_buff += get_method()
            tmp_buff += self.get()
            amount -= 1
        return tmp_buff

    def gets_list(self, amount=None):
        """
        like gets but returns result converted to list
        :param amount:
        :return:
        """
        if not self._available:
            return None
        if not amount:
            amount = self._available
        tmp_buff = []
        while amount and self._available:
            tmp_buff.append(self.get())
            amount -= 1
        return tmp_buff

    def puts(self, string):
        """
        put given string element by element to circular buffer
        :param string:
        :return:
        """
        for elem in string:
            self.put(elem)
        return self

    def __iter__(self):
        return iter(self.gets())

    def __contains__(self, item):
        if len(item) == 1:
            return item in self.buffer
        return item in self.__str__()

    def __str__(self):
        return "".join(self.buffer).replace('\x00', '')

    def str(self):
        """
        will return buffer as string
        :return:
        """
        return "".join(self.buffer)

    def __len__(self):
        return len(self.buffer)


if __name__ == "__main__":
    pass
