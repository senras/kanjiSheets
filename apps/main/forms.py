from django import forms

INPUT_CLASSES = "bg-[#f5f5f5] rounded-lg"


class InputKanjiForm(forms.Form):
    kanjiInput = forms.CharField(widget=forms.Textarea(
        attrs={'class': "border-3 w-full bg-[#DCDCDC] rounded-lg", 'autofocus': 'autofocus', 'placeholder': '日本語を練習しましょう、チバリヨ～'}))
    columnasInput = forms.IntegerField(initial=7, widget=forms.NumberInput(
        attrs={'class': 'border-3 w-10 rounded bg-[#DCDCDC] p-1', 'placeholder': 'Enter number of columns.'}))
