from slugify import slugify

def auto_generate_slug(mapper, connection, target, slug_field: str=None):
    try:
        if slug_field is None:
            raise ValueError('Поле для слага должно быть определено')
        else:
            target['slug'] = slugify(target[slug_field])
    except ValueError as e:
        print(e)