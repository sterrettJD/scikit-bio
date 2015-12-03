# ----------------------------------------------------------------------------
# Copyright (c) 2013--, scikit-bio development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function


class EfficiencyWarning(Warning):
    """Warn about potentially accidental use of inefficient code.

    For example, if a user doesn't have an optimized version of a
    function/algorithm available in their scikit-bio installation, a slower,
    pure-Python implementation may be used instead. This warning can be used to
    let the user know they are using a version of the function that could be
    potentially orders of magnitude slower.

    """
    pass


class RepresentationWarning(Warning):
    """Warn about assumptions made for the successful completion of a process.

    Warn about substitutions, assumptions, or particular alterations that were
    made for the successful completion of a process. For example, if a value
    that is required for a task is not present, a best guess or least
    deleterious value could be used, accompanied by this warning.

    """
    pass