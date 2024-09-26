from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.base import Base


class TargetType(Base):
    __tablename__ = 'targettypes'

    target_type_id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_name = Column(String(255), unique=True, nullable=False)

    # Relationship with Target
    targets = relationship('Target', back_populates='target_type')

    def to_dict(self):
        return {
            'target_type_id': self.target_type_id,
            'target_type_name': self.target_type_name
        }
