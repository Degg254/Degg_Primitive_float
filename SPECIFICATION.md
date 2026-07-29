# Degg Primitive float — SPECIFICATION

## 1. Назначение

Примитивная нода-проброс float-значения. Аналог `CFloat` из ComfyUI-Crystools.

## 2. Файлы

| Файл | Назначение |
|------|-----------|
| `degg_primitive_float.py` | Python-класс `DeggPrimitiveFloat` |
| `__init__.py` | Экспорт маппингов |

## 3. Python: класс DeggPrimitiveFloat

### INPUT_TYPES

| Поле | Тип | По умолчанию | range | step | Описание |
|------|-----|-------------|-------|------|----------|
| `float` | `FLOAT` | `1.0` | `[-sys.float_info.max .. sys.float_info.max]` | `0.01` | Число с плавающей точкой |

### OUTPUT

- `RETURN_TYPES = ("FLOAT",)`
- `RETURN_NAMES = ("float",)`

### Логика process()

1. Принимает float-значение из виджета
2. Возвращает его без изменений

## 4. Категория

`My_custom_nodes`

## 5. Рабочая копия

`D:\ComfyUI_windows_portable\ComfyUI\custom_nodes\Degg_Primitive_float\`
