class Province < ApplicationRecord
  has_many :customers, dependent: :destroy
  validates :abbreviation, :gst, :pst, presence: true
end
