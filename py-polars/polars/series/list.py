from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable

from polars import internals as pli
from polars.series.utils import expr_dispatch
from polars.utils.decorators import deprecate_nonkeyword_arguments

if TYPE_CHECKING:
    from datetime import date, datetime, time

    from polars.expr.expr import Expr
    from polars.polars import PySeries
    from polars.series.series import Series
    from polars.type_aliases import NullBehavior, ToStructStrategy


@expr_dispatch
class ListNameSpace:
    """Series.arr namespace."""

    _accessor = "arr"

    def __init__(self, series: Series):
        self._s: PySeries = series._s

    def lengths(self) -> Series:
        """
        Get the length of the arrays as UInt32.

        Examples
        --------
        >>> s = pl.Series([[1, 2, 3], [5]])
        >>> s.arr.lengths()
        shape: (2,)
        Series: '' [u32]
        [
            3
            1
        ]

        """

    def sum(self) -> Series:
        """Sum all the arrays in the list."""

    def max(self) -> Series:
        """Compute the max value of the arrays in the list."""

    def min(self) -> Series:
        """Compute the min value of the arrays in the list."""

    def mean(self) -> Series:
        """Compute the mean value of the arrays in the list."""

    @deprecate_nonkeyword_arguments()
    def sort(self, descending: bool = False) -> Series:
        """
        Sort the arrays in this column.

        Parameters
        ----------
        descending
            Sort in descending order.

        Examples
        --------
        >>> s = pl.Series("a", [[3, 2, 1], [9, 1, 2]])
        >>> s.arr.sort()
        shape: (2,)
        Series: 'a' [list[i64]]
        [
                [1, 2, 3]
                [1, 2, 9]
        ]
        >>> s.arr.sort(descending=True)
        shape: (2,)
        Series: 'a' [list[i64]]
        [
                [3, 2, 1]
                [9, 2, 1]
        ]

        """
        return (
            pli.wrap_s(self._s)
            .to_frame()
            .select(pli.col(self._s.name()).arr.sort(descending=descending))
            .to_series()
        )

    def reverse(self) -> Series:
        """Reverse the arrays in the list."""

    def unique(self) -> Series:
        """Get the unique/distinct values in the list."""

    def concat(self, other: list[Series] | Series | list[Any]) -> Series:
        """
        Concat the arrays in a Series dtype List in linear time.

        Parameters
        ----------
        other
            Columns to concat into a List Series

        """

    def get(self, index: int | Series | list[int]) -> Series:
        """
        Get the value by index in the sublists.

        So index `0` would return the first item of every sublist
        and index `-1` would return the last item of every sublist
        if an index is out of bounds, it will return a `None`.

        Parameters
        ----------
        index
            Index to return per sublist

        """

    def take(
        self, index: Series | list[int] | list[list[int]], null_on_oob: bool = False
    ) -> Series:
        """
        Take sublists by multiple indices.

        The indices may be defined in a single column, or by sublists in another
        column of dtype ``List``.

        Parameters
        ----------
        index
            Indices to return per sublist
        null_on_oob
            Behavior if an index is out of bounds:
            True -> set as null
            False -> raise an error
            Note that defaulting to raising an error is much cheaper

        """

    def __getitem__(self, item: int) -> Series:
        return self.get(item)

    def join(self, separator: str) -> Series:
        """
        Join all string items in a sublist and place a separator between them.

        This errors if inner type of list `!= Utf8`.

        Parameters
        ----------
        separator
            string to separate the items with

        Returns
        -------
        Series of dtype Utf8

        Examples
        --------
        >>> s = pl.Series([["foo", "bar"], ["hello", "world"]])
        >>> s.arr.join(separator="-")
        shape: (2,)
        Series: '' [str]
        [
            "foo-bar"
            "hello-world"
        ]

        """

    def first(self) -> Series:
        """Get the first value of the sublists."""

    def last(self) -> Series:
        """Get the last value of the sublists."""

    def contains(self, item: float | str | bool | int | date | datetime) -> Series:
        """
        Check if sublists contain the given item.

        Parameters
        ----------
        item
            Item that will be checked for membership

        Returns
        -------
        Boolean mask

        """

    def arg_min(self) -> Series:
        """
        Retrieve the index of the minimal value in every sublist.

        Returns
        -------
        Series of dtype UInt32/UInt64 (depending on compilation)

        """

    def arg_max(self) -> Series:
        """
        Retrieve the index of the maximum value in every sublist.

        Returns
        -------
        Series of dtype UInt32/UInt64 (depending on compilation)

        """

    def diff(self, n: int = 1, null_behavior: NullBehavior = "ignore") -> Series:
        """
        Calculate the n-th discrete difference of every sublist.

        Parameters
        ----------
        n
            Number of slots to shift.
        null_behavior : {'ignore', 'drop'}
            How to handle null values.

        Examples
        --------
        >>> s = pl.Series("a", [[1, 2, 3, 4], [10, 2, 1]])
        >>> s.arr.diff()
        shape: (2,)
        Series: 'a' [list[i64]]
        [
            [null, 1, … 1]
            [null, -8, -1]
        ]

        >>> s.arr.diff(n=2)
        shape: (2,)
        Series: 'a' [list[i64]]
        [
            [null, null, … 2]
            [null, null, -9]
        ]

        >>> s.arr.diff(n=2, null_behavior="drop")
        shape: (2,)
        Series: 'a' [list[i64]]
        [
            [2, 2]
            [-9]
        ]

        """

    def shift(self, periods: int = 1) -> Series:
        """
        Shift values by the given period.

        Parameters
        ----------
        periods
            Number of places to shift (may be negative).

        Examples
        --------
        >>> s = pl.Series("a", [[1, 2, 3, 4], [10, 2, 1]])
        >>> s.arr.shift()
        shape: (2,)
        Series: 'a' [list[i64]]
        [
            [null, 1, … 3]
            [null, 10, 2]
        ]

        """

    def slice(self, offset: int, length: int | None = None) -> Series:
        """
        Slice every sublist.

        Parameters
        ----------
        offset
            Start index. Negative indexing is supported.
        length
            Length of the slice. If set to ``None`` (default), the slice is taken to the
            end of the list.

        Examples
        --------
        >>> s = pl.Series("a", [[1, 2, 3, 4], [10, 2, 1]])
        >>> s.arr.slice(1, 2)
        shape: (2,)
        Series: 'a' [list[i64]]
        [
            [2, 3]
            [2, 1]
        ]

        """

    def head(self, n: int = 5) -> Series:
        """
        Slice the first `n` values of every sublist.

        Parameters
        ----------
        n
            Number of values to return for each sublist.

        Examples
        --------
        >>> s = pl.Series("a", [[1, 2, 3, 4], [10, 2, 1]])
        >>> s.arr.head(2)
        shape: (2,)
        Series: 'a' [list[i64]]
        [
            [1, 2]
            [10, 2]
        ]

        """

    def tail(self, n: int = 5) -> Series:
        """
        Slice the last `n` values of every sublist.

        Parameters
        ----------
        n
            Number of values to return for each sublist.

        Examples
        --------
        >>> s = pl.Series("a", [[1, 2, 3, 4], [10, 2, 1]])
        >>> s.arr.tail(2)
        shape: (2,)
        Series: 'a' [list[i64]]
        [
            [3, 4]
            [2, 1]
        ]

        """

    def explode(self) -> Series:
        """
        Returns a column with a separate row for every list element.

        Returns
        -------
        Exploded column with the datatype of the list elements.

        See Also
        --------
        Series.reshape : Reshape this Series to a flat Series or a Series of Lists.

        Examples
        --------
        >>> s = pl.Series("a", [[1, 2, 3], [4, 5, 6]])
        >>> s.arr.explode()
        shape: (6,)
        Series: 'a' [i64]
        [
            1
            2
            3
            4
            5
            6
        ]

        """

    def count_match(
        self, element: float | str | bool | int | date | datetime | time | Expr
    ) -> Expr:
        """
        Count how often the value produced by ``element`` occurs.

        Parameters
        ----------
        element
            An expression that produces a single value

        """

    def to_struct(
        self,
        n_field_strategy: ToStructStrategy = "first_non_null",
        name_generator: Callable[[int], str] | None = None,
    ) -> Series:
        """
        Convert the series of type ``List`` to a series of type ``Struct``.

        Parameters
        ----------
        n_field_strategy : {'first_non_null', 'max_width'}
            Strategy to determine the number of fields of the struct.
            'first_non_null': set number of fields to the length of the first
            non-zero-length sublist.
            'max_width': set number of fields as max length of all sublists.
        name_generator
            A custom function that can be used to generate the field names.
            Default field names are `field_0, field_1 .. field_n`

        Examples
        --------
        >>> df = pl.DataFrame({"a": [[1, 2, 3], [1, 2]]})
        >>> df.select([pl.col("a").arr.to_struct()])
        shape: (2, 1)
        ┌────────────┐
        │ a          │
        │ ---        │
        │ struct[3]  │
        ╞════════════╡
        │ {1,2,3}    │
        │ {1,2,null} │
        └────────────┘
        >>> df.select(
        ...     [
        ...         pl.col("a").arr.to_struct(
        ...             name_generator=lambda idx: f"col_name_{idx}"
        ...         )
        ...     ]
        ... ).to_series().to_list()
        [{'col_name_0': 1, 'col_name_1': 2, 'col_name_2': 3},
        {'col_name_0': 1, 'col_name_1': 2, 'col_name_2': None}]

        """
        # We set the upper bound to 0.
        # No need to create the proper schema in eager mode.
        s = pli.wrap_s(self)
        return (
            s.to_frame()
            .select(
                pli.col(s.name).arr.to_struct(
                    n_field_strategy, name_generator, upper_bound=0
                )
            )
            .to_series()
        )

    def eval(self, expr: Expr, parallel: bool = False) -> Series:
        """
        Run any polars expression against the lists' elements.

        Parameters
        ----------
        expr
            Expression to run. Note that you can select an element with `pl.first()`, or
            `pl.col()`
        parallel
            Run all expression parallel. Don't activate this blindly.
            Parallelism is worth it if there is enough work to do per thread.

            This likely should not be use in the groupby context, because we already
            parallel execution per group

        Examples
        --------
        >>> df = pl.DataFrame({"a": [1, 8, 3], "b": [4, 5, 2]})
        >>> df.with_columns(
        ...     pl.concat_list(["a", "b"]).arr.eval(pl.element().rank()).alias("rank")
        ... )
        shape: (3, 3)
        ┌─────┬─────┬────────────┐
        │ a   ┆ b   ┆ rank       │
        │ --- ┆ --- ┆ ---        │
        │ i64 ┆ i64 ┆ list[f32]  │
        ╞═════╪═════╪════════════╡
        │ 1   ┆ 4   ┆ [1.0, 2.0] │
        │ 8   ┆ 5   ┆ [2.0, 1.0] │
        │ 3   ┆ 2   ┆ [2.0, 1.0] │
        └─────┴─────┴────────────┘

        """
