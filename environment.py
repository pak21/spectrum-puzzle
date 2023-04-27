import dataclasses
import enum
import typing

class ObjectType(enum.Enum):
    BLOCK_BLACK = enum.auto(),
    BLOCK_BLUE = enum.auto(),
    BLOCK_RED = enum.auto(),
    BLOCK_MAGENTA = enum.auto(),
    BLOCK_GREEN = enum.auto(),
    BLOCK_CYAN = enum.auto(),
    BLOCK_YELLOW = enum.auto(),
    BLOCK_WHITE = enum.auto()

@dataclasses.dataclass
class Board():
    objects: dict[(int, int), ObjectType]
    sources: dict[(int, int), ObjectType]
    sinks: dict[(int, int), list[ObjectType]]

    def pickup_from(self, position):
        obj = self.objects.get(position)
        if obj:
            del self.objects[position]
        return obj

    def drop_at(self, position, obj):
        if position in self.objects:
            return False

        self.objects[position] = obj
        return True

    def step(self):
        for source_location, source_type in self.sources.items():
            if source_location not in self.objects:
                self.objects[source_location] = source_type

        for sink_location, sunk_objects in self.sinks.items():
            obj = self.objects.get(sink_location)
            if obj:
                sunk_objects.append(obj)
                del self.objects[sink_location]
