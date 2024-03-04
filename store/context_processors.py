def dummy(request):
    return {"msg":"hello world"}



def basket_count(request):
    if request.user.is_authenticated:
        count=request.user.cart.cart_item_count
        return {"cart_count":count}
    return {"cart_count":0}

