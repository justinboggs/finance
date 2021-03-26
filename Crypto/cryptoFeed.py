from cryptofeed import FeedHandler
from cryptofeed.exchanges import Coinbase
def nbbo_update(symbol, bid, bid_size, ask, ask_size, bid_feed, ask_feed):
    print(
        f'Pair: {symbol} ' +
        f'Bid Price: {bid:.2f} ' +
        f'Bid Size: {bid_size:.6f} ' +
        f'Bid Feed: {bid_feed} ' +
        f'Ask Price: {ask:.2f} ' +
        f'Ask Size: {ask_size:.6f} ' +
        f'Ask Feed: {ask_feed}'
    )
feed = FeedHandler()
feed.add_nbbo([Coinbase], ['BTC-USD'], nbbo_update)
feed.run()