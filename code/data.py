STOCK = {
    "intro menu": {
        "name": "Stock Exchange Center",
        "content":'''CocaCola (KO): $58 (Dividend) ${linechange}$ 
                Apple (AAPL): $190 (Growth) ${linechange}$ 
                SPDR S&P 500 ETF (SPY): $455 (ETF) ${linechange}$ 
                New Pacific Metal Corp (NEWP): $1.69 (Penny Stock) ${linechange}$ 
                UnitedHealth Group Inc (INH): $546 (Defensive) ${linechange}$ ${linechange}$ 
                [1]   Buy CocaCola ${linechange}$
                [2]   Buy Apple ${linechange}$
                [3]   Buy SPY ${linechange}$
                [4]   Buy NEWP ${linechange}$
                [5]   Buy UNH ${linechange}$
                [Esc] Exit Menu'''
    },
    "option 1": { 
        "name": "CocaCola (KO)",
        "content": '''Stock Type: Dividend ${linechange}$ ${linechange}$
                    Description: Stocks that regularly share profits with shareholders. 
                    Dividend stocks tend to be a very good choice for long term 
                    growth, as they pay the shareholder an income on top of the 
                    stake owned in the company. ''',
        "next option": '''Press 'B' to buy''',
        "result_good": '''Congratulations! Your investment in CocaCola (KO)
                          paid off. You earned a profit from dividends.''',
        "result_bad": '''Unfortunately, CocaCola performed poorly due to intensive competition.''',
        "profit_ratio": 0.08,
        "lose_ratio": 0.06,
    },
    "option 2": { 
        "name": "Apple (AAPL)",
        "content": '''Stock Type: Growth ${linechange}$ ${linechange}$  
                    Description: Stocks that tend to grow faster than their counterparts. 
                    However, in economic downturns, stocks can perform 
                    poorly as these downturns cause question regarding 
                    companies' future growth.''',
        "next option": '''Press 'B' to buy''',
        "result_good": '''Wow! Your investment in Apple (AAPL) performed well. You earned a profit.''',
        "result_bad": '''OMG! Apple performed terribly bad.''',
        "profit_ratio": 0.15,
        "lose_ratio": 0.2,
    },
    "option 3": { 
        "name": "SPDR S&P 500 ETF (SPY)",
        "content": '''Stock Type: ETF ${linechange}$ ${linechange}$ 
                    Description: A collection of securities that tracks an underlying index. For 
                    example, SPY tracks the S&P 500 (Top 500 Stocks on 
                    the market by market cap.) ETFs are beneficial because 
                    they are low cost and allow for diversification. The 
                    downsides are the fees that sometimes come with the purchase of these ETFs.''',
        "next option": '''Press 'B' to buy''',
        "result_good": '''Great choice! SPY, being an ETF, has provided steady growth of 10% over the last 5 years.''',
        "result_bad": '''Unfortunately, SPY has experienced a downturn in recent months due to market volatility.''',
        "profit_ratio": 0.1,
        "lose_ratio": 0.25,
    },
    "option 4": {
        "name": "New Pacific Metals (NEWP)",
        "content": '''Stock Type: Penny Stock ${linechange}$ ${linechange}$ 
                    Description: Stocks that are usually less than $5 per share. These 
                    tend to be like playing the lottery. Sometimes people will 
                    hit it big, but other than that, they are a very risky investment.''',
        "next option": '''Press 'B' to buy''',
        "result_good": '''What a luck! NEWP, being a penny stock, has almost doubled its price within a month!''',
        "result_bad": '''It's a gamble! NEWP, being a penny stock, has shown volatility. It's a high-risk, high-reward play. ${linechange}$ ${linechange}$ 
                         Unfortunately, market conditions take a turn for the worse, causing NEWP to experience a significant drop in value. Your investment is now at a loss, and you find yourself navigating the unpredictable nature of penny stocks. Consider reassessing your investment strategy for the future.''',
        "profit_ratio": 0.8,  # Adjust based on the high-risk nature of penny stocks
        "lose_ratio": 0.6,    # Adjust based on the high-risk nature of penny stocks
    },
    "option 5": { 
        "name": "United Health Group (UNH)",
        "content": '''Stock Type: Defensive ${linechange}$ ${linechange}$  
                    Description: Stocks that have very minimal risk and are generally safer 
                    investments. These stocks tend to grow way slower than 
                    growth stocks, but in times of economic downturn, they 
                    are a great way to keep capital safer.''',
        "next option": '''Press 'B' to buy''',
        "result_good": '''Steady and safe! UNH, being a defensive stock, has provided a reliable investment. Your capital is secure, and you've earned a steady return.''',
        "result_bad": '''Unfortunately, UNH didn't perform as expected due to unforeseen market conditions.''',
        "profit_ratio": 0.06,
        "lose_ratio": 0.05,
    }
}



REAL_ESTATE = {
    "intro menu": {
        "name": "Real Estate Marketplace",            
        "content":'''Elite City Realty (Condo) ${linechange}$ 
                Grand Horizon Estates (Single-Family Home) ${linechange}$ 
                Harmony Meadows Realty (Commercial Building) ${linechange}$ 
                Urban Oasis Properties (Student Housing) ${linechange}$ 
                Evergreen Valley Realty (Vacation Home) ${linechange}$ ${linechange}$ 
                [1]   Invest in Elite City Realty ${linechange}$
                [2]   Invest in Grand Horizon Estates ${linechange}$
                [3]   Invest in Harmony Meadows Realty ${linechange}$
                [4]   Invest in Urban Oasis Properties ${linechange}$
                [5]   Invest in Evergreen Valley Realty ${linechange}$
                [Esc] Exit Menu'''
    },
    "option 1": { 
        "name": "Elite City Realty",
        "content": '''Real Estate Type: Condo ${linechange}$ ${linechange}$ 
                      Description: Luxurious condominiums located in the heart of the city, offering modern amenities and breathtaking views. ''',
        "next option": '''Press 'B' to invest''',
        "result_good": '''Marvelous! Elite City Realty becomes the talk of the town, with your condominiums gaining immense popularity. The surge in demand leads to a remarkable profit of $[?]. Your investment not only appreciates but becomes a symbol of luxury living in the city. Your foresight in selecting prime real estate has truly paid off.''',
        "result_bad": '''Despite the luxurious appeal, unexpected maintenance issues arise, requiring immediate attention. The cost of repairs amounts to $[?], impacting your profit margins. Even the most upscale properties can come with unforeseen challenges.''',
        "profit_ratio": 0.09,
        "lose_ratio": 0.05,
    },
    "option 2": { 
        "name": "Grand Horizon Estates",
        "content": '''Real Estate Type: Single-Family Home ${linechange}$ ${linechange}$ 
                      Description: Spacious and elegant single-family homes in a peaceful suburban setting, perfect for families.''',
        "next option": '''Press 'B' to invest''',
        "result_good": '''Outstanding choice! Grand Horizon Estates becomes a community favorite, with your single-family homes gaining attention for their unique design and family-friendly environment. As demand surges, you secure a substantial profit of $[?] on your investment. Your strategic vision and commitment to quality have truly paid off.''',
        "result_bad": '''Unexpected economic challenges impact the real estate market in your region. The demand for single-family homes dwindles, leading to a decline in property values and potential financial losses of $[?]. It's a reminder of the ever-changing dynamics of the real estate market.''',
        "profit_ratio": 0.09,
        "lose_ratio": 0.05,
    },
    "option 3": { 
        "name": "Harmony Meadows Realty",
        "content": '''Real Estate Type: Commercial Building ${linechange}$ ${linechange}$ 
                      Description: Prime commercial properties tailored to businesses seeking strategic locations and top-notch facilities.''',
        "next option": '''Press 'B' to invest''',
        "result_good": '''Congratulations! The strategic location and top-notch facilities of your commercial property attract high-profile businesses. Your property becomes a lucrative asset, generating an impressive $[?] in rental income. It's a testament to your smart investment choices and the thriving commercial real estate market.''',
        "result_bad": '''Unfortunately, a downturn in the local economy has led to a decline in demand for commercial spaces. Your property faces prolonged vacancies, resulting in a significant loss of $[?] Consider reevaluating the market conditions for future investments.''',
        "profit_ratio": 0.08,
        "lose_ratio": 0.06,
    },
    "option 4": { 
        "name": "Urban Oasis Properties",
        "content": '''Real Estate Type: Student Housing ${linechange}$ ${linechange}$ 
                      Description: Comfortable and convenient housing options designed to meet the unique needs of students, fostering a vibrant academic community.''',
        "next option": '''Press 'B' to invest''',
        "result_good": '''Excellent choice! The demand for student housing reaches new heights, and your property becomes a sought-after residence. Enjoy a substantial profit of $[?] on your investment, capitalizing on the flourishing student housing market. It's a testament to your foresight and understanding of the evolving needs of academic communities.''',
        "result_bad": '''Unexpected challenges arise as regulatory changes impact student housing policies. Your property faces increased restrictions and compliance costs of $[?], leading to a decline in rental income and potential financial setbacks. It's a tough lesson in navigating the dynamic landscape of student housing investments.''',
        "profit_ratio": 0.07,
        "lose_ratio": 0.08,
    },
    "option 5": { 
        "name": "Evergreen Valley Realty",
        "content": '''Real Estate Type: Vacation Home ${linechange}$ ${linechange}$ 
                      Description: Charming vacation homes nestled in scenic landscapes, providing a tranquil escape for relaxation and leisure.''',
        "next option": '''Press 'B' to invest''',
        "result_good": '''Congratulations! Your vacation home becomes a popular retreat, attracting a surge in demand. Enjoy a substantial profit of $[?] as more people seek the tranquil escape your property offers. It's a testament to the appeal of your vacation home and the growing interest in the scenic landscapes it provides.''',
        "result_bad": '''Unfortunately, changing travel trends and a decrease in consumer spending impact the demand for vacation homes. Your property experiences a decline in bookings and a reduction in value, resulting in a $[?] financial setback . It's a reminder of the unpredictable nature of the vacation rental market.''',
        "profit_ratio": 0.1,
        "lose_ratio": 0.04,
    },
}



CASINO = {
    "intro menu": {
        "name": "Bay 168 Casino",            
        "content":'''Welcome! Sic bo is a game of pure chance. You simply bet on the results of the roll of three dice, each bet will cost $50. Please place your bet below: ${linechange}$ ${linechange}$ 
                    [1]   Sum of the 3 rolls is an EVEN number! (1-to-1 payouts) ${linechange}$
                    [2]   Sum of the 3 rolls is an ODD number! (1-to-1 payouts) ${linechange}$
                    [3]   Sum of the 3 rolls is > 9! (2-to-1 payouts) ${linechange}$
                    [4]   Sum of the 3 rolls is <= 9! (2-to-1 payouts) ${linechange}$
                    [5]   Sum of the 3 rolls is exactly 18! (20-to-1 payouts) ${linechange}$
                    [Esc] Exit Menu
                  '''
    },
    "title": "Roll Results",
    "content": '''Dice 1 rolled: [dice1] ${linechange}$ Dice 2 rolled: [dice2] ${linechange}$ Dice 3 rolled: [dice3] ${linechange}$ ${linechange}$ ''',
    "option 1": { 
        "result_good": '''Congrats! Sum of rolls [total] is an even number. You just won $[?].''',
        "result_bad": '''Not my day! Sum of rolls [total] is NOT an even number. You lost $[?] this round.''',
    },
    "option 2": { 
        "result_good": '''Congrats! Sum of rolls [total] is an odd number. You just won $[?].''',
        "result_bad": '''Not my day! Sum of rolls [total] is NOT an odd number. You lost $[?] this round.''',
    },
    "option 3": { 
        "result_good": '''Congrats! Sum of rolls [total] is larger than 9. You just won $[?].''',
        "result_bad": '''Not my day! Sum of rolls [total] is NOT larger than 9. You lost $[?] this round.''',
    },
    "option 4": { 
        "result_good": '''Congrats! Sum of rolls [total] is either less than or equal to 9. You just won $[?].''',
        "result_bad": '''Not my day! Sum of rolls [total] is neither less than nor equal to 9. You lost $[?] this round.''',
    },
    "option 5": { 
        "result_good": '''Congrats! Sum of rolls [total] is exactly 18. You won a fortune of $[?].''',
        "result_bad": '''Not my day! Sum of rolls [total] is NOT exactly 18. You lost $[?] this round.''',
    },
}



LOTTERY = {
    "intro menu": {
        "name": "Lottery",            
        "content":'''Welcome to the lottery! Each round costs $50 to play ${linechange}$ ${linechange}$ 
                    [1]   Play Lottery! ${linechange}$
                    [Esc] Exit Menu
                  '''
    },
    "title": "Lottery Outcome",
    "content": '''Hello! ${linechange}$ ${linechange}$ ''',
    "option 1": { 
        "result_good": '''Congratulations! You won [gain]! Your new balance is $[?].''',
        "result_bad": '''Sorry, you didn't win this time. Your balance is now $[?].''',
    },
}