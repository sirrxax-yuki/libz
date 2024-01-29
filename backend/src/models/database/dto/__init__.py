from sqlalchemy.orm import declarative_base


__all__ = [ 'Base', 'to_dict', 'to_string' ]


Base = declarative_base()

def to_dict(dto: Base) -> dict[str, str]:
    return { k: str(v) for k, v in vars(dto).items() if not k.startswith('relation') and not k.startswith('_sa') }

def to_string(dto: Base) -> str:
    return f"<{dto.__class__}: {', '.join([ k + ': ' + str(v) for k, v in vars(dto).items() if not k.startswith('relation') and not k.startswith('_sa') ])}>"
