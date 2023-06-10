from django.core.exceptions import ValidationError
import django_filters as filters

# from users.models import User
from recipes.models import Ingredient, Recipe, Tag


class TagsMultipleChoiceField(
        filters.fields.MultipleChoiceField):
    def validate(self, value):
        if self.required and not value:
            raise ValidationError(
                self.error_messages['required'],
                code='required')
        for val in value:
            if val in self.choices and not self.valid_value(val):
                raise ValidationError(
                    self.error_messages['invalid_choice'],
                    code='invalid_choice',
                    params={'value': val},)


class TagsFilter(filters.AllValuesMultipleFilter):
    field_class = TagsMultipleChoiceField


class IngredientFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeFilter(filters.FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all(),
    )

    is_favorited = filters.BooleanFilter(method='filter_is_favorited')
    is_in_shopping_cart = filters.BooleanFilter(
        method='filter_is_in_shopping_cart'
    )

    class Meta:
        model = Recipe
        fields = ('tags', 'author',)

    def filter_is_favorited(self, queryset, name, value):
        user = self.request.user
        if value and not user.is_anonymous:
            return queryset.filter(favorites__user=user)
        return queryset

    def filter_is_in_shopping_cart(self, queryset, name, value):
        user = self.request.user
        if value and not user.is_anonymous:
            return queryset.filter(shopping_cart__user=user)
        return queryset

# class RecipeFilter(filters.FilterSet):
#     author = filters.ModelChoiceFilter(
#         queryset=User.objects.all())
#     is_in_shopping_cart = filters.BooleanFilter(
#         widget=filters.widgets.BooleanWidget(),
#         label='В корзине.')
#     is_favorited = filters.BooleanFilter(
#         widget=filters.widgets.BooleanWidget(),
#         label='В избранных.')
#     tags = filters.AllValuesMultipleFilter(
#         field_name='tags__slug',
#         label='Ссылка')

#     class Meta:
#         model = Recipe
#         fields = ['is_favorited', 'is_in_shopping_cart', 'author', 'tags']

