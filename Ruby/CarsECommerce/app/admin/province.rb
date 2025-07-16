ActiveAdmin.register Province do
    permit_params :abbreviation, :gst, :pst

    form do |f|
        f.semantic_errors
        f.inputs do
        f.input :abbreviation
        f.input :gst
        f.input :pst
      end
      f.actions
    end
  end
  