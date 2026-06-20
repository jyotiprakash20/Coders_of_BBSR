#Simple chaining
# class Hash:
#     def __init__(self, buckets):
#         self.bucket_count= buckets

#         self.table = [[] for i in range(self.bucket_count)]
    
#     def insert(self, key):
#         index= self.get_hash_index(key)

#         self.table[index].append(key)

#     def remove(self, key):
#         index = self.get_hash_index(key)

#         if key in self.table[index]:
#             self.table[index].remove(key)

#     def display(self):
#         for i in range(self.bucket_count):
#             print(i, end='')

#             for key in self.table[i]:
#                 print('-->', key, end='')
#             print()

#     def get_hash_index(self, key):
#         return key % self.bucket_count

# if __name__ == '__main__':
#     keys= [10, 20, 15, 7, 32, 5, 12, 25]

#     hash_table= Hash(8)

#     for key in keys:
#         hash_table.insert(key)
#     hash_table.display()
#     hash_table.remove(12)
#     hash_table.display()

#Chaining with rehashing
class HashTable:
    def __init__(self, buckets):
        self.bucket_count=buckets
        self.num_of_ele=0
        self.table =[[] for i in range(buckets)]

    def insert(self, key):
        while self.get_load_factor() > 0.5:
            self.rehash()

        index = self.get_hash_index(key)

        self.table[index].append(key)
        self.num_of_ele +=1

    def remove(self, key):
        index= self.get_hash_index(key)

        if key in self.table[index]:
            self.table[index].remove(key)
            self.num_of_ele -=1
    def display(self):
        for i in range(self.bucket_count):
            print(i, end='')
            for key in self.table[i]:
                print('-->', key, end='')
            print()
    
    def get_hash_index(self, key):
        return key % self.bucket_count
    
    def get_load_factor(self):
        return self.num_of_ele / self.bucket_count
    
    def rehash(self):
        old_table = self.table
        self.bucket_count *=2
        self.table = [[] for i in range(self.bucket_count)]
        self.num_of_ele =0

        for bucket in old_table:
            for key in bucket:
                self.insert(key)

if __name__ == '__main__':

    keys= [12, 45, 2, 5 , 7, 8]
    hashTable= HashTable(8)

    for key in keys:
        hashTable.insert(key)

    hashTable.remove(8)
    hashTable.display()
    hashTable.insert(19)

    print('\nAfter rehashing')
    hashTable.display()

