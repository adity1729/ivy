from typing import Any
import tensorflow as tf


promotion_table = {
    ("bool", "bool"): "bool",
    ("int8", "int8"): "int8",
    ("int8", "int16"): "int16",
    ("int8", "int32"): "int32",
    ("int8", "int64"): "int64",
    ("int16", "int16"): "int16",
    ("int16", "int32"): "int32",
    ("int16", "int64"): "int64",
    ("int32", "int32"): "int32",
    ("int32", "int64"): "int64",
    ("int64", "int64"): "int64",
    ("uint8", "int8"): "int16",
    ("uint8", "int16"): "int16",
    ("uint8", "int32"): "int32",
    ("uint8", "int64"): "int64",
    ("uint8", "uint8"): "uint8",
    ("uint8", "uint16"): "uint16",
    ("uint8", "uint32"): "uint32",
    ("uint8", "uint64"): "uint64",
    ("uint16", "int8"): "int32",
    ("uint16", "int16"): "int32",
    ("uint16", "int32"): "int32",
    ("uint16", "int64"): "int64",
    ("uint16", "uint16"): "uint16",
    ("uint16", "uint32"): "uint32",
    ("uint16", "uint64"): "uint64",
    ("uint32", "int8"): "int64",
    ("uint32", "int16"): "int64",
    ("uint32", "int32"): "int64",
    ("uint32", "int64"): "int64",
    ("uint32", "uint32"): "uint32",
    ("uint32", "uint64"): "uint64",
    ("uint64", "uint64"): "uint64",
    ("float16", "float16"): "float16",
    ("float16", "float32"): "float32",
    ("float16", "float64"): "float64",
    ("float32", "float32"): "float32",
    ("float32", "float64"): "float64",
    ("float64", "float64"): "float64",
    ("bool", "int8"): "int8",
    ("bool", "int16"): "int16",
    ("bool", "int32"): "int32",
    ("bool", "int64"): "int64",
    ("bool", "uint8"): "uint8",
    ("bool", "uint16"): "uint16",
    ("bool", "uint32"): "uint32",
    ("bool", "uint64"): "uint64",
    ("bool", "float16"): "float16",
    ("bool", "float32"): "float32",
    ("bool", "float64"): "float64",
    ("bool", "bfloat16"): "bfloat16",
    ("bool", "complex64"): "complex64",
    ("bool", "complex128"): "complex128",
    ("int8", "float16"): "float16",
    ("int8", "float32"): "float32",
    ("int8", "float64"): "float64",
    ("int8", "bfloat16"): "bfloat16",
    ("int8", "complex64"): "complex64",
    ("int8", "complex128"): "complex128",
    ("int16", "float32"): "float32",
    ("int16", "float64"): "float64",
    ("int16", "complex64"): "complex64",
    ("int16", "complex128"): "complex128",
    ("int32", "float64"): "float64",
    ("int32", "complex128"): "complex128",
    ("int64", "float64"): "float64",
    ("int64", "complex128"): "complex128",
    ("uint8", "float16"): "float16",
    ("uint8", "float32"): "float32",
    ("uint8", "float64"): "float64",
    ("uint8", "bfloat16"): "bfloat16",
    ("uint8", "complex64"): "complex64",
    ("uint8", "complex128"): "complex128",
    ("uint16", "float32"): "float32",
    ("uint16", "float64"): "float64",
    ("uint16", "complex64"): "complex64",
    ("uint16", "complex128"): "complex128",
    ("uint32", "float64"): "float64",
    ("uint32", "complex128"): "complex128",
    ("uint64", "int8"): "float64",
    ("uint64", "int16"): "float64",
    ("uint64", "int32"): "float64",
    ("uint64", "int64"): "float64",
    ("uint64", "float64"): "float64",
    ("uint64", "complex128"): "complex128",
    ("float16", "bfloat16"): "float32",
    ("float16", "complex64"): "complex64",
    ("float16", "complex128"): "complex128",
    ("float32", "complex64"): "complex64",
    ("float32", "complex128"): "complex128",
    ("float64", "complex64"): "complex128",
    ("float64", "complex128"): "complex128",
    ("bfloat16", "float16"): "float32",
    ("bfloat16", "float32"): "float32",
    ("bfloat16", "float64"): "float64",
    ("bfloat16", "bfloat16"): "bfloat16",
    ("bfloat16", "complex64"): "complex64",
    ("bfloat16", "complex128"): "complex128",
    ("complex64", "float64"): "complex128",
    ("complex64", "complex64"): "complex64",
    ("complex64", "complex128"): "complex128",
    ("complex128", "complex128"): "complex128",
    ("float16", "int16"): "float32",
    ("float16", "int32"): "float64",
    ("float16", "int64"): "float64",
    ("float16", "uint16"): "float32",
    ("float16", "uint32"): "float64",
    ("float16", "uint64"): "float64",
    ("float32", "int32"): "float64",
    ("float32", "int64"): "float64",
    ("float32", "uint32"): "float64",
    ("float32", "uint64"): "float64",
    ("bfloat16", "int16"): "float32",
    ("bfloat16", "int32"): "float64",
    ("bfloat16", "int64"): "float64",
    ("bfloat16", "uint16"): "float32",
    ("bfloat16", "uint32"): "float64",
    ("bfloat16", "uint64"): "float64",
    ("complex64", "int32"): "complex128",
    ("complex64", "int64"): "complex128",
    ("complex64", "uint32"): "complex128",
    ("complex64", "uint64"): "complex128",
}
array_api_promotion_table = {
    ("bool", "bool"): "bool",
    ("int8", "int8"): "int8",
    ("int8", "int16"): "int16",
    ("int8", "int32"): "int32",
    ("int8", "int64"): "int64",
    ("int16", "int16"): "int16",
    ("int16", "int32"): "int32",
    ("int16", "int64"): "int64",
    ("int32", "int32"): "int32",
    ("int32", "int64"): "int64",
    ("int64", "int64"): "int64",
    ("uint8", "int8"): "int16",
    ("uint8", "int16"): "int16",
    ("uint8", "int32"): "int32",
    ("uint8", "int64"): "int64",
    ("uint8", "uint8"): "uint8",
    ("uint8", "uint16"): "uint16",
    ("uint8", "uint32"): "uint32",
    ("uint8", "uint64"): "uint64",
    ("uint16", "int8"): "int32",
    ("uint16", "int16"): "int32",
    ("uint16", "int32"): "int32",
    ("uint16", "int64"): "int64",
    ("uint16", "uint16"): "uint16",
    ("uint16", "uint32"): "uint32",
    ("uint16", "uint64"): "uint64",
    ("uint32", "int8"): "int64",
    ("uint32", "int16"): "int64",
    ("uint32", "int32"): "int64",
    ("uint32", "int64"): "int64",
    ("uint32", "uint32"): "uint32",
    ("uint32", "uint64"): "uint64",
    ("uint64", "uint64"): "uint64",
    ("float16", "float16"): "float16",
    ("float16", "float32"): "float32",
    ("float16", "float64"): "float64",
    ("float32", "float32"): "float32",
    ("float32", "float64"): "float64",
    ("float64", "float64"): "float64",
}
tf.experimental.numpy.experimental_enable_numpy_behavior(True)


def tensorflow_exists(x: Any, /):
    return x is not None


def tensorflow_default(
    x: Any,
    /,
    default_val: Any,
    *,
    catch_exceptions: bool = False,
    rev: bool = False,
    with_callable: bool = False,
):
    with_callable = catch_exceptions or with_callable
    if rev:
        x, default_val = default_val, x
    if with_callable:
        x_callable = callable(x)
        default_callable = callable(default_val)
    else:
        x_callable = False
        default_callable = False
    if catch_exceptions:
        try:
            x = x() if x_callable else x
        except Exception:
            return default_val() if default_callable else default_val
    else:
        x = x() if x_callable else x
    return (
        x
        if tensorflow_exists(x)
        else default_val() if default_callable else default_val
    )