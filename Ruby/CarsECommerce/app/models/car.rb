class Car < ApplicationRecord
  belongs_to :car_model, optional: true
  has_many :order_items, dependent: :destroy

  has_one_attached :image

  validates :name, :description, :price, :quantity, presence: true
  validates :price, :quantity, numericality: true
end
