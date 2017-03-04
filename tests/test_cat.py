def test_noise():
    import pets.cat.noise
    assert pets.cat.noise.make() == 'meow!'

def test_noise_from_cat():
    from pets import cat
    assert cat.noise.make() == 'meow!'

def test_noise_from_pets_cat():
    from pets.cat import noise
    assert noise.make() == 'meow!'
