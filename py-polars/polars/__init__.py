import os

from polars import api
from polars.config import Config
from polars.convert import (
    from_arrow,
    from_dataframe,
    from_dict,
    from_dicts,
    from_numpy,
    from_pandas,
    from_records,
)

# TODO remove need for wrap_df
from polars.dataframe import (
    DataFrame,
    wrap_df,  # noqa: F401
)
from polars.datatypes import (
    DATETIME_DTYPES,
    DURATION_DTYPES,
    FLOAT_DTYPES,
    INTEGER_DTYPES,
    NUMERIC_DTYPES,
    TEMPORAL_DTYPES,
    Binary,
    Boolean,
    Categorical,
    DataType,
    Date,
    Datetime,
    Decimal,
    Duration,
    Field,
    Float32,
    Float64,
    Int8,
    Int16,
    Int32,
    Int64,
    List,
    Null,
    Object,
    Struct,
    Time,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
    Unknown,
    Utf8,
)
from polars.exceptions import (
    ArrowError,
    ColumnNotFoundError,
    ComputeError,
    DuplicateError,
    InvalidOperationError,
    NoDataError,
    PanicException,
    SchemaError,
    SchemaFieldNotFoundError,
    ShapeError,
    StructFieldNotFoundError,
)
from polars.expr.expr import Expr
from polars.functions.eager import (
    align_frames,
    concat,
    cut,
    date_range,
    get_dummies,
    ones,
    zeros,
)
from polars.functions.lazy import (
    all,
    any,
    apply,
    arange,
    arg_sort_by,
    arg_where,
    argsort_by,
    avg,
    coalesce,
    col,
    collect_all,
    concat_list,
    concat_str,
    corr,
    count,
    cov,
    cumfold,
    cumreduce,
    cumsum,
    duration,
    element,
    exclude,
    first,
    fold,
    format,
    from_epoch,
    groups,
    head,
    last,
    lit,
    map,
    max,
    mean,
    median,
    min,
    n_unique,
    pearson_corr,
    quantile,
    reduce,
    repeat,
    select,
    spearman_rank_corr,
    std,
    struct,
    sum,
    tail,
    var,
)
from polars.functions.lazy import date_ as date
from polars.functions.lazy import datetime_ as datetime
from polars.functions.lazy import list_ as list
from polars.functions.whenthen import when
from polars.io import (
    read_avro,
    read_csv,
    read_csv_batched,
    read_database,
    read_delta,
    read_excel,
    read_ipc,
    read_ipc_schema,
    read_json,
    read_ndjson,
    read_parquet,
    read_parquet_schema,
    read_sql,
    scan_csv,
    scan_delta,
    scan_ds,
    scan_ipc,
    scan_ndjson,
    scan_parquet,
    scan_pyarrow_dataset,
)
from polars.lazyframe import LazyFrame

# TODO: remove need for wrap_s
from polars.series import wrap_s  # noqa: F401
from polars.series.series import Series
from polars.sql import SQLContext
from polars.string_cache import StringCache, toggle_string_cache, using_string_cache
from polars.type_aliases import PolarsDataType
from polars.utils import (
    build_info,
    get_idx_type,
    get_index_type,
    show_versions,
    threadpool_size,
)
from polars.utils.polars_version import get_polars_version as _get_polars_version

__version__: str = _get_polars_version()
del _get_polars_version

__all__ = [
    "api",
    "exceptions",
    # exceptions/errors
    "ArrowError",
    "ColumnNotFoundError",
    "ComputeError",
    "DuplicateError",
    "InvalidOperationError",
    "NoDataError",
    "PanicException",
    "SchemaError",
    "SchemaFieldNotFoundError",
    "ShapeError",
    "StructFieldNotFoundError",
    # core classes
    "DataFrame",
    "Expr",
    "LazyFrame",
    "Series",
    # polars.datatypes
    "Binary",
    "Boolean",
    "Categorical",
    "DataType",
    "Date",
    "Datetime",
    "Decimal",
    "Duration",
    "Field",
    "Float32",
    "Float64",
    "Int16",
    "Int32",
    "Int64",
    "Int8",
    "List",
    "Null",
    "Object",
    "Struct",
    "Time",
    "UInt16",
    "UInt32",
    "UInt64",
    "UInt8",
    "Unknown",
    "Utf8",
    # polars.datatypes: dtype groups
    "DATETIME_DTYPES",
    "DURATION_DTYPES",
    "FLOAT_DTYPES",
    "INTEGER_DTYPES",
    "NUMERIC_DTYPES",
    "TEMPORAL_DTYPES",
    # polars.type_aliases
    "PolarsDataType",
    # polars.io
    "read_avro",
    "read_csv",
    "read_csv_batched",
    "read_database",
    "read_delta",
    "read_excel",
    "read_ipc",
    "read_ipc_schema",
    "read_json",
    "read_ndjson",
    "read_parquet",
    "read_parquet_schema",
    "read_sql",
    "scan_csv",
    "scan_delta",
    "scan_ds",
    "scan_ipc",
    "scan_ndjson",
    "scan_parquet",
    "scan_pyarrow_dataset",
    # polars.stringcache
    "StringCache",
    "toggle_string_cache",
    "using_string_cache",
    # polars.config
    "Config",
    # polars.internals.whenthen
    "when",
    # polars.internals.functions
    "align_frames",
    "arg_where",
    "concat",
    "cut",
    "date_range",
    "element",
    "get_dummies",
    "ones",
    "repeat",
    "zeros",
    # polars.internals.lazy_functions
    "all",
    "any",
    "apply",
    "arange",
    "arg_sort_by",
    "argsort_by",
    "avg",
    "coalesce",
    "col",
    "collect_all",
    "concat_list",
    "concat_str",
    "corr",
    "count",
    "cov",
    "cumfold",
    "cumreduce",
    "cumsum",
    "date",  # named date_, see import above
    "datetime",  # named datetime_, see import above
    "duration",
    "exclude",
    "first",
    "fold",
    "format",
    "from_epoch",
    "groups",
    "head",
    "last",
    "list",  # named list_, see import above
    "lit",
    "map",
    "max",
    "mean",
    "median",
    "min",
    "n_unique",
    "pearson_corr",
    "quantile",
    "reduce",
    "select",
    "spearman_rank_corr",
    "std",
    "struct",
    "sum",
    "tail",
    "var",
    "var",
    # polars.convert
    "from_arrow",
    "from_dataframe",
    "from_dict",
    "from_dicts",
    "from_numpy",
    "from_pandas",
    "from_records",
    # sql
    "SQLContext",
    # utils
    "build_info",
    "get_idx_type",
    "get_index_type",
    "show_versions",
    "threadpool_size",
]

os.environ["POLARS_ALLOW_EXTENSION"] = "true"
