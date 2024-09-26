from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Float
from sqlalchemy.orm import relationship
from config.base import Base


class City(Base):
    __tablename__ = 'cities'

    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(200), unique=True, nullable=False)
    country_id = Column(Integer, ForeignKey('countries.country_id'), nullable=False)
    latitude = Column(DECIMAL, nullable=True)
    longitude = Column(DECIMAL, nullable=True)

    # Relationships
    country = relationship('Country', back_populates='cities')
    targets = relationship('Target', back_populates='city')

    def to_dict(self):
        return {
            'city_id': self.city_id,
            'city_name': self.city_name,
            'country_id': self.country_id,
            'latitude': float(self.latitude) if self.latitude else None,
            'longitude': float(self.longitude) if self.longitude else None,
            # Include related entities if needed
        }
