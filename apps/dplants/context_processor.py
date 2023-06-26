def totalCart(request):
    total=0
    if "cart" in request.session.keys():
        for key, value in request.session["cart"].items():
            total += int(value["prices"])
    return {"totalCart": total }