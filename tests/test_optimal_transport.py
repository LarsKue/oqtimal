
import jax.numpy as jnp

def test_optimal_transport():
    from oqtimal import optimal_transport

    x = jnp.array([1, 2, 3])
    y = jnp.array([4, 5, 6])

    x, y = optimal_transport(x, y)
