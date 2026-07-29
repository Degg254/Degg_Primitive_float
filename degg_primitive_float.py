import sys


class DeggPrimitiveFloat:
    """
    ──────────────────────────────────────────────
    Degg Primitive Float
    ──────────────────────────────────────────────
    Назначение:
      Примитивная нода-проброс float-значения.
      Аналог CFloat из ComfyUI-Crystools.

    Входы (widget):
      float (FLOAT) — число с плавающей точкой.
        default: 1.0
        range:  [-sys.float_info.max .. sys.float_info.max]
        step:   0.01

    Выходы:
      float (FLOAT) — переданное значение без изменений.

    Категория:
      My_custom_nodes

    Использование:
      Удобна для задания констант, управления seed,
      коэффициентов масштабирования и т.д.
    ──────────────────────────────────────────────
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float": ("FLOAT", {
                    "default": 1.0,
                    "min": -sys.float_info.max,
                    "max": sys.float_info.max,
                    "step": 0.01,
                }),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("float",)
    FUNCTION = "process"
    CATEGORY = "My_custom_nodes"
    DESCRIPTION = "Primitive float passthrough. Compatible with Crystools CFloat."

    def process(self, float=1.0):
        return (float,)


NODE_CLASS_MAPPINGS = {
    "DeggPrimitiveFloat": DeggPrimitiveFloat,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DeggPrimitiveFloat": "Degg Primitive float",
}