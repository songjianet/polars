from __future__ import annotations

from typing import TYPE_CHECKING

from polars.series.utils import expr_dispatch

if TYPE_CHECKING:
    from polars.polars import PySeries
    from polars.series.series import Series
    from polars.type_aliases import TransferEncoding


@expr_dispatch
class BinaryNameSpace:
    """Series.bin namespace."""

    _accessor = "bin"

    def __init__(self, series: Series):
        self._s: PySeries = series._s

    def contains(self, lit: bytes) -> Series:
        """
        Check if binaries in Series contain a binary substring.

        Parameters
        ----------
        lit
            The binary substring to look for

        Returns
        -------
        Boolean mask

        """

    def ends_with(self, sub: bytes) -> Series:
        """
        Check if string values end with a binary substring.

        Parameters
        ----------
        sub
            Suffix substring.

        """

    def starts_with(self, sub: bytes) -> Series:
        """
        Check if values start with a binary substring.

        Parameters
        ----------
        sub
            Prefix substring.

        """

    def decode(self, encoding: TransferEncoding, *, strict: bool = True) -> Series:
        """
        Decode a value using the provided encoding.

        Parameters
        ----------
        encoding : {'hex', 'base64'}
            The encoding to use.
        strict
            Raise an error if the underlying value cannot be decoded,
            otherwise mask out with a null value.

        """

    def encode(self, encoding: TransferEncoding) -> Series:
        """
        Encode a value using the provided encoding.

        Parameters
        ----------
        encoding : {'hex', 'base64'}
            The encoding to use.

        Returns
        -------
        Binary array with values encoded using provided encoding

        """
