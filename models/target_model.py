from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.base import Base

class Target(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    target_industry = Column(String(255), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.city_id'), nullable=False)
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'), nullable=True)
    target_priority = Column(Integer, nullable=True)

    city = relationship('City', back_populates='targets')
    target_type = relationship('TargetType', back_populates='targets')

    def to_dict(self):
        return {
            'target_id': self.target_id,
            'target_industry': self.target_industry,
            'city_id': self.city_id,
            'target_type_id': self.target_type_id,
            'target_priority': self.target_priority,

        }