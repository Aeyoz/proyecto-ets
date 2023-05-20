def automatic_code(cls: object) -> int:
    cls.code += 1
    new_code = cls.code
    return new_code