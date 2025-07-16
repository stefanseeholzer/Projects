class CarMake < ApplicationRecord
  has_many :car_makes, dependent: :destroy
  validates :name, :description, presence: true
end
