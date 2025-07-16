class CarModel < ApplicationRecord
  belongs_to :car_make
  has_many :cars, dependent: :destroy

  validates :name, :description, presence: true
end
