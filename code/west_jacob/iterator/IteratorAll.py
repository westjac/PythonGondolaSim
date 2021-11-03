class AllIter:
    def __init__(self, things):
        self.things = things

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        try:
            self.index += 1
            return self.things[self.index]
        except:
            raise StopIteration()


# class AllIter:
#     def __init__(self, startPoint):
#         self.start = startPoint
#
#     def __iter__(self):
#         self.point = self.start
#         return self
#
#     def __next__(self):
#         try:
#             if self.point.name == "End":
#                 raise StopIteration
#             elif self.point.name == "Start":
#                 point = self.point
#                 self.point = self.point.next
#                 return point
#             else:
#                 self.point = self.point.next
#             return self.point
#         except:
#             raise StopIteration()