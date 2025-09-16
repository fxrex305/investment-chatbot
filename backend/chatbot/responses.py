import re

def get_investment_response(message):
    message = message.lower()

    # --- Flexible spelling match for S.AG Private --- #
    if re.search(r"\bs\.?a?g\b|\bsag\b|\bs\.ag\b", message, re.IGNORECASE):
        return (
            "S.AG Private is a New Zealand-based, privately owned and independent financial advisory firm. "
            "We specialise in personalised portfolio management for high-net-worth individuals, family offices, and charitable organisations.\n\n"
            "We are known for client-centric service, genuine independence, and clear, research-driven solutions. "
            "Our portfolios are always tailored—combining global and home bias, risk-adjusted alternatives, and proactive reviews. "
            "With rigorous manager screening, full transparency, and 24/7 online portfolio access, S.AG Private truly stands apart in helping you secure and grow your wealth the Kiwi way. — REX"
        )
    
    # --- S.AG Private  --- #
    if re.search(r"\bs\.?a?g\b|\bsag\b|\bSAG\b|\bs\.ag\b", message, re.IGNORECASE):
        return (
            "S.AG Private is a New Zealand-based, privately owned and independent financial advisory firm. "
            "We specialise in personalised portfolio management for high-net-worth individuals, family offices, and charitable organisations.\n\n"
            "What makes us unique is our unwavering commitment to clients: portfolios are tailored to each investor’s objectives and risk appetite, "
            "with clear communication, proactive reviews, and a focus on transparent, unbiased recommendations. Our client-centric philosophy emphasises "
            "capital preservation, long-term growth, and global diversification—balanced with New Zealand stewardship and values.\n\n"
            "At S.AG Private, our offerings include access to alternative assets, global and Australasian equities, and rigorous, research-driven manager selection. "
            "We are constantly reviewing and adapting portfolios to remain aligned with your goals and responsive to changing markets. Security is paramount: "
            "we use independent custodians and provide comprehensive performance and tax reporting.\n\n"
            "In short: you receive genuine independence, comprehensive advice, and a partner dedicated to helping you achieve financial peace of mind, preserve "
            "your wealth, and build a lasting legacy. — REX"
        )
    
    # Unique proposition and philosophy
    if "philosophy" in message or "unique proposition" in message:
        return (
            "At S.AG Private, our investment philosophy centres on client-centricity, independence, "
            "and a commitment to security. We blend robust experience with research-driven decisions, "
            "offering objective, unbiased advice to help you preserve wealth, achieve long-term growth, "
            "and build a legacy for future generations. — REX"
        )

    # Client centric / personalised service
    if "client" in message or "personal" in message or "tailored" in message:
        return (
            "Our approach is genuinely client centric. We listen actively, deeply understand your aspirations, "
            "and tailor portfolios to your individual objectives and risk appetite. Our relationship is built around "
            "clear communication and ongoing reviews to keep your portfolio aligned with your goals. — REX"
        )

    # Security, independence, transparency
    if "security" in message or "independent" in message or "unbiased" in message:
        return (
            "S.AG Private is privately owned and independent, with no affiliations that could create conflicts. "
            "We provide transparency, safeguard your assets with independent custodians, and offer detailed performance "
            "and taxation reports, giving you true peace of mind. — REX"
        )

    # Diversification
    if "diversification" in message or "diversify" in message:
        return (
            "Diversification is a cornerstone of our risk management approach. We construct globally balanced portfolios, "
            "typically allocating across at least 15 uncorrelated assets, industries, and geographies. "
            "In New Zealand, we also maintain ‘home bias’ where appropriate, balancing this with global diversification "
            "for smoother returns across market cycles. — REX"
        )

    # Portfolio structure/asset allocation
    if "asset allocation" in message or "portfolio structure" in message:
        return (
            "Portfolio structure underpins investment outcomes. We offer five robust portfolio models — Conservative, "
            "Moderately Conservative, Balanced, Growth, and High Growth. For example, a Conservative portfolio might include "
            "20% cash and 60% fixed interest, while a High Growth approach weights heavily towards Australasian and International Equities. "
            "Every allocation is reviewed monthly to ensure ongoing alignment with your needs and market conditions. — REX"
        )

    # Core investment principles
    if "core principle" in message or "belief" in message or "investment principle" in message:
        return (
            "Our core investment principles include: comprehensive global diversification, "
            "accepting the inherent link between risk and return, focusing on asset allocation as the main driver of performance, "
            "leveraging skilled active management, and maintaining a disciplined, long-term perspective. — REX"
        )

    # Active/passive management, beta/alpha
    if "active" in message or "passive" in message or "alpha" in message or "beta" in message:
        return (
            "We use a blend of active and passive management. Passive strategies provide market exposure (beta), "
            "while active managers are carefully selected to seek outperformance (alpha) based on research and experience. "
            "This combination allows for robust, adaptable portfolios across different market conditions. — REX"
        )

    # Alternative assets
    if "alternative asset" in message or "private equity" in message or "real estate" in message or "hedge fund" in message or "private credit" in message:
        return (
            "Alternative assets are a strategic pillar for us, offering diversification and uncorrelated returns. "
            "We allocate through carefully screened top-tier fund managers — in private equity, real estate, hedge funds, "
            "commodities, and private credit. We target enhanced returns, inflation protection, and stability, "
            "with allocation ranges typically 5–15% depending on portfolio type and client profile. — REX"
        )

    # Alternative asset selection and due diligence
    if "allocation" in message and "alternative" in message or "fund selection" in message:
        return (
            "We screen alternative funds using specific metrics: for private equity, we assess track record, IRR, MOIC, and sector expertise; "
            "for real estate, factors like asset location, type, and manager skill are paramount. Our due diligence prioritises "
            "outperformance, reporting transparency, performance-aligned fees, and operational rigour. — REX"
        )

    # Risk management, risk, capital preservation
    if "risk" in message or "capital preservation" in message or "risk management" in message:
        return (
            "Risk is integral to investing. Our framework balances risk and return to suit each client. "
            "We spread risk using a broad array of asset classes and fund managers — in both New Zealand and globally — and focus deeply on preserving capital. "
            "Diversification, active monitoring, and disciplined selection help buffer against volatility and market downturns. — REX"
        )

    # Fund manager selection and evaluation criteria
    if "manager" in message or "due diligence" in message or "manager selection" in message or "fund manager" in message:
        return (
            "Fund manager selection is rigorous and multi-layered. Our key criteria include proven performance over market cycles, "
            "alignment of incentives and philosophy, and operational excellence. We literally ask: "
            "— Does the manager have flexibility for capital preservation?\n"
            "— How does their process differ from the benchmark?\n"
            "— Are their incentives aligned with your success?\n"
            "— Can they manage fund capacity responsibly?\n"
            "We prefer managers with strong research backgrounds, meaningful skin in the game, and a culture of transparency. — REX"
        )

    # ETF selection, evaluation
    if "etf" in message or "exchange traded fund" in message:
        return (
            "ETF selection at S.AG Private is research-driven: we evaluate fund size (favouring those >A$500m), liquidity, cost efficiency (OER and tracking difference), "
            "and replication method (preferring physical or sampling); synthetic ETFs are only considered when necessary. "
            "We consider the underlying index methodology and market exposure to ensure each ETF fits within your portfolio’s risk and opportunity needs. — REX"
        )

    # Equities and equity selection criteria
    if "equity" in message or "equities" in message or "stock" in message or "shares" in message:
        return (
            "Equity selection at S.AG Private is meticulous. We require: gross margins >40%, positive EPS growth, net income margin >20%, "
            "debt levels low, and a preference for companies with expanding retained earnings. Preference is given to firms with over 25% revenue "
            "from international sources, for added diversification. Research, fundamentals, and the right market exposure guide our equity selections. — REX"
        )

    # Strategies for different investment horizons or risk profiles
    if "long term" in message or "time horizon" in message or "goal" in message or "strategy" in message:
        return (
            "We tailor strategies to each client’s time horizon and goals. Longer horizons allow for higher allocation to growth assets, "
            "while shorter or more defensive needs lean towards cash and fixed interest holdings. Every strategy is evaluated and rebalanced monthly to remain true to your evolving objectives and risk profile. — REX"
        )

    # Broader asset class questions
    if "asset class" in message or "cash" in message or "fixed interest" in message or "property" in message or "credit" in message or "commodities" in message:
        return (
            "Our portfolios comprise a strategic mix of cash, fixed interest, property, equities, credit, and alternative assets. "
            "Allocation to each asset class is calibrated to your specific objectives and reflects our view on current market opportunities. "
            "For example, fixed interest and cash may make up 20–80% in conservative portfolios, while growth aspirations justify more equity and alternative asset exposure. — REX"
        )

    # Greetings
    if "hello" in message or "hi" in message or "kia ora" in message or "greetings" in message:
        return (
            "Hello, and welcome to S.AG Private. I am REX, your wise and experienced investment companion. "
            "Ask me questions, and I'll try to answer with clarity and care."
        )

    # Farewell
    if "bye" in message or "farewell" in message or "goodbye" in message or "see you" in message:
        return (
            "Thank you for your time. If you seek further investment wisdom, I’m always here to assist. Mā te wā — REX"
        )

    # Catch-all default fallback
    return (
        "REX here. I draw on the philosophy and process of S.AG Private for every answer. "
        "Please ask about portfolio construction, diversification, risk management, alternative assets, fund selection, or any investment theme that interests you."
    )
    
    # If no known match, always respond with handoff:
    return (
        "Great question. I will get my colleague to get back to you."
    )