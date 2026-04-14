---
title: EERD diagram update
category: Projects
priority: Medium
starred: None
created: 2025-11-06T22:23:58.072020
updated: 2025-11-06T22:26:12.043388
dg-publish: true
---
# EERD diagram update

**Priority:** Medium

## Conversation

### Assistant

Here’s a complete draw.io XML for an EERD that applies your fixes: weak Options/Futures, ETF as a Security subtype, Quote vs Historical_Price, Order_Book, Corporate_Action, Clearing_House, Trading_Session, Greeks, and temporal attributes on time-varying entities and relationships.

```xml
<mxfile host="app.diagrams.net" modified="2025-11-06T22:05:00.000Z" agent="5.0" version="22.1.0" etag="gsdh-eerd" type="device">
  <diagram name="GSDH-EERD" id="eerd-diagram">
    <mxGraphModel dx="1600" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2000" pageHeight="1400" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- SUPERTYPE: Security -->
        <mxCell id="security" value="Security" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff;" vertex="1" parent="1">
          <mxGeometry x="620" y="40" width="160" height="70" as="geometry"/>
        </mxCell>
        <mxCell id="sec-id" value="security_id (PK)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="500" y="20" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="sec-ticker" value="ticker (UQ)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="500" y="70" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="sec-name" value="name" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="800" y="20" width="100" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="sec-status" value="status" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="800" y="70" width="100" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_s1" edge="1" parent="1" source="sec-id" target="security"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_s2" edge="1" parent="1" source="sec-ticker" target="security"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_s3" edge="1" parent="1" source="sec-name" target="security"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_s4" edge="1" parent="1" source="sec-status" target="security"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- ISA triangle for Security -->
        <mxCell id="isa1" value="ISA" style="triangle;whiteSpace=wrap;html=1;direction=south;" vertex="1" parent="1">
          <mxGeometry x="690" y="130" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_isa1" edge="1" parent="1" source="security" target="isa1"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- SUBTYPE: Stock -->
        <mxCell id="stock" value="Stock" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="420" y="220" width="150" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="stock-company" value="company_name" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="340" y="200" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="stock-shares" value="shares_outstanding" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="340" y="250" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_st1" edge="1" parent="1" source="stock-company" target="stock"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_st2" edge="1" parent="1" source="stock-shares" target="stock"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_isa1_stock" edge="1" parent="1" source="isa1" target="stock"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- SUBTYPE: ETF -->
        <mxCell id="etf" value="ETF" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="620" y="220" width="150" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="etf-mgr" value="fund_manager" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="580" y="290" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="etf-exp" value="expense_ratio" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="700" y="290" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_etf1" edge="1" parent="1" source="etf-mgr" target="etf"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_etf2" edge="1" parent="1" source="etf-exp" target="etf"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_isa1_etf" edge="1" parent="1" source="isa1" target="etf"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- SUBTYPE GROUP: Derivatives (supertype for Options/Futures) -->
        <mxCell id="deriv" value="Derivatives" style="rounded=0;whiteSpace=wrap;html=1;dashed=1;" vertex="1" parent="1">
          <mxGeometry x="840" y="220" width="150" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="e_isa1_deriv" edge="1" parent="1" source="isa1" target="deriv"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- ISA triangle for Derivatives -->
        <mxCell id="isa2" value="ISA" style="triangle;whiteSpace=wrap;html=1;direction=south;" vertex="1" parent="1">
          <mxGeometry x="915" y="300" width="40" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_deriv_isa2" edge="1" parent="1" source="deriv" target="isa2"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- WEAK ENTITY: Options (identifying by underlying Security + attrs) -->
        <mxCell id="options" value="Options (WEAK)" style="rounded=0;whiteSpace=wrap;html=1;strokeWidth=2;dashed=1;" vertex="1" parent="1">
          <mxGeometry x="780" y="360" width="170" height="70" as="geometry"/>
        </mxCell>
        <mxCell id="opt-under-fk" value="underlying_security_id (FK, PK&#x394;)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="740" y="330" width="160" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="opt-exp" value="expiration (PK&#x394;)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="740" y="410" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="opt-strike" value="strike_price (PK&#x394;)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="920" y="410" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="opt-type" value="type (call/put) (PK&#x394;)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="920" y="330" width="140" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_op1" edge="1" parent="1" source="opt-under-fk" target="options"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_op2" edge="1" parent="1" source="opt-exp" target="options"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_op3" edge="1" parent="1" source="opt-strike" target="options"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_op4" edge="1" parent="1" source="opt-type" target="options"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_isa2_opt" edge="1" parent="1" source="isa2" target="options"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- WEAK ENTITY: Futures (identifying by underlying Security + delivery) -->
        <mxCell id="futures" value="Futures (WEAK)" style="rounded=0;whiteSpace=wrap;html=1;strokeWidth=2;dashed=1;" vertex="1" parent="1">
          <mxGeometry x="1060" y="360" width="170" height="70" as="geometry"/>
        </mxCell>
        <mxCell id="fut-under-fk" value="underlying_security_id (FK, PK&#x394;)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1020" y="330" width="160" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="fut-delivery" value="delivery_date (PK&#x394;)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1020" y="410" width="140" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="fut-size" value="contract_size" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1200" y="410" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_fu1" edge="1" parent="1" source="fut-under-fk" target="futures"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_fu2" edge="1" parent="1" source="fut-delivery" target="futures"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_fu3" edge="1" parent="1" source="fut-size" target="futures"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_isa2_fut" edge="1" parent="1" source="isa2" target="futures"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- Underlying identifying relationship -->
        <mxCell id="underlying" value="Underlying (identifying)" style="rhombus;whiteSpace=wrap;html=1;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="780" y="300" width="110" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="e_ul1" edge="1" parent="1" source="stock" target="underlying"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_ul2" edge="1" parent="1" source="underlying" target="options"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_ul3" edge="1" parent="1" source="underlying" target="futures"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_ul1c" value="1" style="text;html=1;align=center;verticalAlign=middle;resizable=0;autosize=1;" vertex="1" parent="1"><mxGeometry x="520" y="290" width="30" height="20" as="geometry"/></mxCell>
        <mxCell id="e_ul2c" value="N" style="text;html=1;align=center;verticalAlign=middle;resizable=0;autosize=1;" vertex="1" parent="1"><mxGeometry x="860" y="350" width="30" height="20" as="geometry"/></mxCell>
        <mxCell id="e_ul3c" value="N" style="text;html=1;align=center;verticalAlign=middle;resizable=0;autosize=1;" vertex="1" parent="1"><mxGeometry x="1060" y="350" width="30" height="20" as="geometry"/></mxCell>

        <!-- Exchange -->
        <mxCell id="exchange" value="Exchange" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="180" y="40" width="150" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="exch-name" value="name (PK)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="90" y="20" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="exch-ccy" value="currency" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="90" y="70" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_ex1" edge="1" parent="1" source="exch-name" target="exchange"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_ex2" edge="1" parent="1" source="exch-ccy" target="exchange"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- Lists_On with temporal validity -->
        <mxCell id="lists_on" value="Lists_On (valid_from, valid_to)" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="380" y="40" width="130" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="e_lo1" edge="1" parent="1" source="exchange" target="lists_on"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_lo2" edge="1" parent="1" source="lists_on" target="security"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_lo1c" value="1" style="text;html=1;align=center;verticalAlign=middle;resizable=0;autosize=1;" vertex="1" parent="1"><mxGeometry x="340" y="50" width="30" height="20" as="geometry"/></mxCell>
        <mxCell id="e_lo2c" value="N" style="text;html=1;align=center;verticalAlign=middle;resizable=0;autosize=1;" vertex="1" parent="1"><mxGeometry x="560" y="50" width="30" height="20" as="geometry"/></mxCell>

        <!-- Order_Book and relation -->
        <mxCell id="order_book" value="Order_Book" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="180" y="140" width="150" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="ob-id" value="order_book_id (PK)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="90" y="120" width="140" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="ob-type" value="book_type (L1/L2)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="90" y="170" width="140" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_ob1" edge="1" parent="1" source="ob-id" target="order_book"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_ob2" edge="1" parent="1" source="ob-type" target="order_book"><mxGeometry relative="1" as="geometry"/></mxCell>

        <mxCell id="has_ob" value="Has_Order_Book" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="320" y="140" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="e_hob1" edge="1" parent="1" source="exchange" target="has_ob"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_hob2" edge="1" parent="1" source="has_ob" target="order_book"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_hob3" edge="1" parent="1" source="has_ob" target="security"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- Trader, Order, Trade (unchanged core), plus Clearing_House and Trading_Session -->
        <mxCell id="trader" value="Trader" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="180" y="520" width="150" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="trader-id" value="trader_id (PK)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="90" y="500" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="trader-type" value="type" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="90" y="550" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_tr1" edge="1" parent="1" source="trader-id" target="trader"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_tr2" edge="1" parent="1" source="trader-type" target="trader"><mxGeometry relative="1" as="geometry"/></mxCell>

        <mxCell id="order" value="Order" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="380" y="520" width="150" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="order-id" value="order_id (PK)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="300" y="500" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="order-qty" value="quantity" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="300" y="550" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="order-side" value="side (buy/sell)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="540" y="550" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_or1" edge="1" parent="1" source="order-id" target="order"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_or2" edge="1" parent="1" source="order-qty" target="order"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_or3" edge="1" parent="1" source="order-side" target="order"><mxGeometry relative="1" as="geometry"/></mxCell>

        <mxCell id="places" value="Places" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="300" y="520" width="80" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="e_pl1" edge="1" parent="1" source="trader" target="places"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_pl2" edge="1" parent="1" source="places" target="order"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_pl1c" value="1" style="text;html=1;align=center;verticalAlign=middle;resizable=0;autosize=1;" vertex="1" parent="1"><mxGeometry x="270" y="530" width="30" height="20" as="geometry"/></mxCell>
        <mxCell id="e_pl2c" value="N" style="text;html=1;align=center;verticalAlign=middle;resizable=0;autosize=1;" vertex="1" parent="1"><mxGeometry x="360" y="530" width="30" height="20" as="geometry"/></mxCell>

        <mxCell id="trade" value="Trade" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="600" y="520" width="150" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="trade-id" value="trade_id (PK)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="590" y="600" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="trade-price" value="price" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="720" y="600" width="100" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="trade-time" value="timestamp" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="840" y="600" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_trd1" edge="1" parent="1" source="trade-id" target="trade"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_trd2" edge="1" parent="1" source="trade-price" target="trade"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_trd3" edge="1" parent="1" source="trade-time" target="trade"><mxGeometry relative="1" as="geometry"/></mxCell>

        <mxCell id="executes" value="Executes" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="530" y="520" width="70" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="e_exe1" edge="1" parent="1" source="order" target="executes"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_exe2" edge="1" parent="1" source="executes" target="trade"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- Clearing_House and relation -->
        <mxCell id="clearing" value="Clearing_House" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="820" y="520" width="160" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="clearing-id" value="clearing_house_id (PK)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1000" y="500" width="160" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_cl1" edge="1" parent="1" source="clearing-id" target="clearing"><mxGeometry relative="1" as="geometry"/></mxCell>

        <mxCell id="cleared_by" value="Cleared_By" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="760" y="520" width="70" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="e_cb1" edge="1" parent="1" source="trade" target="cleared_by"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_cb2" edge="1" parent="1" source="cleared_by" target="clearing"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- Trading_Session and relation -->
        <mxCell id="session" value="Trading_Session" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1000" y="600" width="170" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="sess-id" value="session_id (PK)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1180" y="580" width="130" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="sess-type" value="type (pre/open/close/after)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1180" y="630" width="170" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_ts1" edge="1" parent="1" source="sess-id" target="session"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_ts2" edge="1" parent="1" source="sess-type" target="session"><mxGeometry relative="1" as="geometry"/></mxCell>

        <mxCell id="occurs_in" value="Occurs_In" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="920" y="600" width="70" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="e_oi1" edge="1" parent="1" source="trade" target="occurs_in"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_oi2" edge="1" parent="1" source="occurs_in" target="session"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- Quote (real-time, temporal) -->
        <mxCell id="quote" value="Quote (temporal)" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="620" y="360" width="150" height="70" as="geometry"/>
        </mxCell>
        <mxCell id="q-id" value="quote_id (PK)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="520" y="340" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="q-bidask" value="bid, ask, last" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="520" y="390" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="q-valid" value="valid_from, valid_to" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="520" y="440" width="150" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_q1" edge="1" parent="1" source="q-id" target="quote"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_q2" edge="1" parent="1" source="q-bidask" target="quote"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_q3" edge="1" parent="1" source="q-valid" target="quote"><mxGeometry relative="1" as="geometry"/></mxCell>

        <mxCell id="has_quote" value="Has_Quote" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="600" y="290" width="110" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="e_hq1" edge="1" parent="1" source="security" target="has_quote"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_hq2" edge="1" parent="1" source="has_quote" target="quote"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_hq1c" value="1" style="text;html=1;align=center;verticalAlign=middle;resizable=0;autosize=1;" vertex="1" parent="1"><mxGeometry x="700" y="110" width="30" height="20" as="geometry"/></mxCell>
        <mxCell id="e_hq2c" value="N" style="text;html=1;align=center;verticalAlign=middle;resizable=0;autosize=1;" vertex="1" parent="1"><mxGeometry x="640" y="340" width="30" height="20" as="geometry"/></mxCell>

        <!-- Historical_Price (temporal by date and valid range) -->
        <mxCell id="hist" value="Historical_Price (temporal)" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="820" y="460" width="170" height="70" as="geometry"/>
        </mxCell>
        <mxCell id="h-date" value="price_date (PK&#x394;)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="780" y="540" width="140" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="h-ohlc" value="open, high, low, close, volume" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="940" y="540" width="180" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="h-valid" value="valid_from, valid_to" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="780" y="590" width="150" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_h1" edge="1" parent="1" source="h-date" target="hist"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_h2" edge="1" parent="1" source="h-ohlc" target="hist"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_h3" edge="1" parent="1" source="h-valid" target="hist"><mxGeometry relative="1" as="geometry"/></mxCell>

        <mxCell id="has_hist" value="Has_History" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="720" y="240" width="110" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="e_hh1" edge="1" parent="1" source="security" target="has_hist"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_hh2" edge="1" parent="1" source="has_hist" target="hist"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- Greeks for Options -->
        <mxCell id="greeks" value="Greeks (temporal)" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="780" y="650" width="180" height="70" as="geometry"/>
        </mxCell>
        <mxCell id="g-delta" value="delta, gamma, theta, vega, rho" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="980" y="650" width="190" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="g-valid" value="valid_from, valid_to" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="980" y="700" width="150" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_g1" edge="1" parent="1" source="g-delta" target="greeks"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_g2" edge="1" parent="1" source="g-valid" target="greeks"><mxGeometry relative="1" as="geometry"/></mxCell>

        <mxCell id="has_greeks" value="Has_Greeks" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="760" y="600" width="110" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="e_hg1" edge="1" parent="1" source="options" target="has_greeks"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_hg2" edge="1" parent="1" source="has_greeks" target="greeks"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- Market_Sector and Belongs_To -->
        <mxCell id="sector" value="Market_Sector" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="380" y="350" width="160" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="sector-name" value="sector_name (PK)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="300" y="330" width="140" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_se1" edge="1" parent="1" source="sector-name" target="sector"><mxGeometry relative="1" as="geometry"/></mxCell>

        <mxCell id="belongs_to" value="Belongs_To" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="360" y="290" width="110" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="e_bt1" edge="1" parent="1" source="stock" target="belongs_to"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_bt2" edge="1" parent="1" source="belongs_to" target="sector"><mxGeometry relative="1" as="geometry"/></mxCell>

        <!-- Index and Contains (M:N with temporal attributes) -->
        <mxCell id="index" value="Index" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1280" y="220" width="150" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="idx-name" value="index_name (PK)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1200" y="200" width="150" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="idx-base" value="base_value" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1200" y="250" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_ix1" edge="1" parent="1" source="idx-name" target="index"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_ix2" edge="1" parent="1" source="idx-base" target="index"><mxGeometry relative="1" as="geometry"/></mxCell>

        <mxCell id="contains" value="Contains (weight, effective_from, effective_to)" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1020" y="220" width="200" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="e_ct1" edge="1" parent="1" source="stock" target="contains"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_ct2" edge="1" parent="1" source="contains" target="index"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_ct1c" value="M" style="text;html=1;align=center;verticalAlign=middle;resizable=0;autosize=1;" vertex="1" parent="1"><mxGeometry x="520" y="230" width="30" height="20" as="geometry"/></mxCell>
        <mxCell id="e_ct2c" value="N" style="text;html=1;align=center;verticalAlign=middle;resizable=0;autosize=1;" vertex="1" parent="1"><mxGeometry x="1240" y="230" width="30" height="20" as="geometry"/></mxCell>

        <!-- Corporate_Action and relation -->
        <mxCell id="corp" value="Corporate_Action" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1280" y="360" width="170" height="70" as="geometry"/>
        </mxCell>
        <mxCell id="corp-id" value="action_id (PK)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1470" y="340" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="corp-type" value="type (split, dividend,...)" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1470" y="390" width="160" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="corp-eff" value="effective_date" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1470" y="440" width="130" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e_ca1" edge="1" parent="1" source="corp-id" target="corp"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_ca2" edge="1" parent="1" source="corp-type" target="corp"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_ca3" edge="1" parent="1" source="corp-eff" target="corp"><mxGeometry relative="1" as="geometry"/></mxCell>

        <mxCell id="affects" value="Affects" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1160" y="360" width="90" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="e_af1" edge="1" parent="1" source="corp" target="affects"><mxGeometry relative="1" as="geometry"/></mxCell>
        <mxCell id="e_af2" edge="1" parent="1" source="affects" target="security"><mxGeometry relative="1" as="geometry"/></mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Notes:
- Temporal fields added: `valid_from/valid_to` on Quote, Historical_Price, Lists_On, Contains, Greeks.
- Options and Futures are weak via identifying relationship to `Stock` through `Underlying`.
- ETF is a subtype of `Security`.
- Added `Order_Book`, `Corporate_Action`, `Clearing_House`, `Trading_Session`, and linking relationships.
- Use this XML directly in draw.io to render the EERD.

---

