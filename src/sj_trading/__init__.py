import shioaji as sj

def main() -> None:
    print("Hello from sj-trading!")

    api = sj.Shioaji(simulation=True) # 模擬模式
    api.login(
        api_key="FPs61fotK4wDDmEMrTvwGQ1Gk2TWUD19vLqJYbBxvHsN",     # 請修改此處
        secret_key="5425RG3epQpUHw1EHE2FyW7cjnE3Bph65Zij6FDMy6RQ"   # 請修改此處
    )


    contract = api.Contracts.Stocks.TSE["2890"]

    # 證券委託單 - 請修改此處
    order = api.Order(
        price=18,                                       # 價格
        quantity=1,                                     # 數量
        action=sj.constant.Action.Buy,                  # 買賣別
        price_type=sj.constant.StockPriceType.LMT,      # 委託價格類別
        order_type=sj.constant.OrderType.ROD,           # 委託條件
        account=api.stock_account                       # 下單帳號
    )

    # 下單
    trade = api.place_order(contract, order)
    
    print(trade)