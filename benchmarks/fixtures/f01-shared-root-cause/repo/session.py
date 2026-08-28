from dataclasses import dataclass


@dataclass(frozen=True)
class Session:
    user_id: str
    expires_at: int
    revoked: bool = False


def is_active(session: Session, now: int) -> bool:
    return not session.revoked and session.expires_at >= now


def can_read(session: Session, now: int) -> bool:
    return not session.revoked and session.expires_at >= now


def can_write(session: Session, now: int) -> bool:
    return not session.revoked and session.expires_at >= now
