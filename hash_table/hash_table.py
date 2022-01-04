"""hashlib -> 해쉬 함수를 이용하기 위한 모듈
typing -> TypeHint를 위한 모듈"""
import hashlib
from typing import Any

class HashTable :
    """HashTable를 생성하는 Class"""

    def __init__(self, lens) -> None:
        self.hash_table = [[None] for _ in range(lens)]
        self.lens = lens

    def hashing(self, key : Any) -> int :
        """Hash 함수를 이용해서 사용자가 입력한 key를 해싱.

        Args:
            key (Any): [시용자가 입력한 키 값.]

        Returns:
            int: [Hash 함수를 이용해서 생성한 hex 값을 정수형으로 리턴.]
        """
        hashing = hashlib.sha256()
        hashing.update(key.encode())
        hash_hex = hashing.hexdigest()
        return int(hash_hex, 16)

    def create_key(self, hash_hex : int) -> int :
        """Hash 값을 사용자가 입력한 HashTable 길이로 나누어서 HashTable에 저장한 Index 번호를 생성.

        Args:
            hash_hex (int): [Hash 함수를 통해 생성한 Hash 값.]

        Returns:
            int: [HashTable에 저장한 Index 번호.]
        """
        return hash_hex % self.lens

    def insert(self, key : Any, values : Any) -> None :
        """HashTable에 값 집어넣는 함수.

        Args:
            key (Any): [HashTable에서 사용될 Key 값.]
            values (Any): [저장할 값.]

        Returns:
            None: [return이 없고 HashTable에 바로 값을 저장.]
        """
        hash_hex = self.hashing(key)
        key = self.create_key(hash_hex)

        if self.hash_table[key][0] is not None :
            for _, for_values in enumerate(self.hash_table[key]) :
                if for_values[0] == hash_hex:
                    for_values[1] = values
                    return 0

                else :
                    continue

            self.hash_table[key].append([hash_hex, values])

        else :
            self.hash_table[key] = [[hash_hex, values]]

    def print(self, key : Any) -> None :
        """사용자가 입력한 키 값을 통해 Slot에 있는 데이터를 출력하는 함수.

        Args:
            key (Any): [조회할 Slot의 키 값.]

        Returns:
            None: [return 하지 않고 값을 출력.]
        """
        hash_hex = self.hashing(key)
        key = self.create_key(hash_hex)

        if self.hash_table[key][0] is None :
            return None

        else :
            for _, for_values in enumerate(self.hash_table[key]) :
                if for_values[0] == hash_hex:
                    print(for_values[1])

            return None
