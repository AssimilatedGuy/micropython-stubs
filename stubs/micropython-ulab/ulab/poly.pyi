import ulab
from ulab import _ArrayLike as _ArrayLike

def polyfit(y: _ArrayLike, degree: int) -> ulab.array: ...
def polyval(p: _ArrayLike, x: _ArrayLike) -> ulab.array: ...
