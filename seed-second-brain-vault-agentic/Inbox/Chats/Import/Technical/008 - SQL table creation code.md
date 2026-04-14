---
title: SQL table creation code
category: Technical
priority: Medium
starred: None
created: 2025-11-26T22:01:21.100983
updated: 2025-11-26T22:11:57.564090
dg-publish: true
---
# SQL table creation code

**Priority:** Medium

## Conversation

### Assistant

Below are **clean SQL INSERT statements** to fully repopulate:

- `item_categories`  
- `shops` (IDs 1–5 must already exist)  
- `shop_hours`  
- `shop_hour_exceptions`  
- `items`  
- `item_variants`

All statements are **static**, ready to paste into MariaDB.

---

# **1. ITEM CATEGORIES**
```sql
INSERT INTO item_categories (category_name) VALUES
('Food & Beverages'),
('Electronics'),
('Books & Magazines'),
('Clothing & Accessories'),
('Souvenirs & Gifts'),
('Health & Beauty'),
('Travel Essentials');
```

---

# **2. SHOP HOURS (FOR SHOP IDs 1–5)**  
**Open daily 06:00–22:00 except Sunday for even shop IDs (2,4).**  
Days: **0 = Monday … 6 = Sunday**

```sql
-- Shop 1 (all days open)
INSERT INTO shop_hours (shop_id, day_of_week, open_time, close_time, is_closed) VALUES
(1,0,'06:00:00','22:00:00',0),
(1,1,'06:00:00','22:00:00',0),
(1,2,'06:00:00','22:00:00',0),
(1,3,'06:00:00','22:00:00',0),
(1,4,'06:00:00','22:00:00',0),
(1,5,'06:00:00','22:00:00',0),
(1,6,'06:00:00','22:00:00',0);

-- Shop 2 (Sunday closed)
INSERT INTO shop_hours (shop_id, day_of_week, open_time, close_time, is_closed) VALUES
(2,0,'06:00:00','22:00:00',0),
(2,1,'06:00:00','22:00:00',0),
(2,2,'06:00:00','22:00:00',0),
(2,3,'06:00:00','22:00:00',0),
(2,4,'06:00:00','22:00:00',0),
(2,5,'06:00:00','22:00:00',0),
(2,6,NULL,NULL,1);

-- Shop 3 (all days open)
INSERT INTO shop_hours (shop_id, day_of_week, open_time, close_time, is_closed) VALUES
(3,0,'06:00:00','22:00:00',0),
(3,1,'06:00:00','22:00:00',0),
(3,2,'06:00:00','22:00:00',0),
(3,3,'06:00:00','22:00:00',0),
(3,4,'06:00:00','22:00:00',0),
(3,5,'06:00:00','22:00:00',0),
(3,6,'06:00:00','22:00:00',0);

-- Shop 4 (Sunday closed)
INSERT INTO shop_hours (shop_id, day_of_week, open_time, close_time, is_closed) VALUES
(4,0,'06:00:00','22:00:00',0),
(4,1,'06:00:00','22:00:00',0),
(4,2,'06:00:00','22:00:00',0),
(4,3,'06:00:00','22:00:00',0),
(4,4,'06:00:00','22:00:00',0),
(4,5,'06:00:00','22:00:00',0),
(4,6,NULL,NULL,1);

-- Shop 5 (all days open)
INSERT INTO shop_hours (shop_id, day_of_week, open_time, close_time, is_closed) VALUES
(5,0,'06:00:00','22:00:00',0),
(5,1,'06:00:00','22:00:00',0),
(5,2,'06:00:00','22:00:00',0),
(5,3,'06:00:00','22:00:00',0),
(5,4,'06:00:00','22:00:00',0),
(5,5,'06:00:00','22:00:00',0),
(5,6,'06:00:00','22:00:00',0);
```

---

# **3. SHOP HOUR EXCEPTIONS**  
Static example dates:

- Christmas: `2025-12-25` closed  
- New Year Reduced: `2026-01-01`  
- Canada Day: `2026-07-01` closed  
- Thanksgiving (2nd Monday of Oct 2026): `2026-10-12` reduced  
- Special Event: `2025-12-30` extended  

```sql
-- Christmas (closed)
INSERT INTO shop_hour_exceptions (shop_id, exception_date, is_closed, reason) VALUES
(1,'2025-12-25',1,'Christmas Day'),
(2,'2025-12-25',1,'Christmas Day'),
(3,'2025-12-25',1,'Christmas Day'),
(4,'2025-12-25',1,'Christmas Day'),
(5,'2025-12-25',1,'Christmas Day');

-- New Year Reduced Hours
INSERT INTO shop_hour_exceptions (shop_id, exception_date, open_time, close_time, is_closed, reason) VALUES
(1,'2026-01-01','10:00:00','18:00:00',0,'New Year Reduced Hours'),
(2,'2026-01-01','10:00:00','18:00:00',0,'New Year Reduced Hours'),
(3,'2026-01-01','10:00:00','18:00:00',0,'New Year Reduced Hours'),
(4,'2026-01-01','10:00:00','18:00:00',0,'New Year Reduced Hours'),
(5,'2026-01-01','10:00:00','18:00:00',0,'New Year Reduced Hours');

-- Canada Day (closed)
INSERT INTO shop_hour_exceptions (shop_id, exception_date, is_closed, reason) VALUES
(1,'2026-07-01',1,'Canada Day'),
(2,'2026-07-01',1,'Canada Day'),
(3,'2026-07-01',1,'Canada Day'),
(4,'2026-07-01',1,'Canada Day'),
(5,'2026-07-01',1,'Canada Day');

-- Thanksgiving (reduced)
INSERT INTO shop_hour_exceptions (shop_id, exception_date, open_time, close_time, is_closed, reason) VALUES
(1,'2026-10-12','08:00:00','20:00:00',0,'Thanksgiving Reduced Hours'),
(2,'2026-10-12','08:00:00','20:00:00',0,'Thanksgiving Reduced Hours'),
(3,'2026-10-12','08:00:00','20:00:00',0,'Thanksgiving Reduced Hours'),
(4,'2026-10-12','08:00:00','20:00:00',0,'Thanksgiving Reduced Hours'),
(5,'2026-10-12','08:00:00','20:00:00',0,'Thanksgiving Reduced Hours');

-- Special Event (extended)
INSERT INTO shop_hour_exceptions (shop_id, exception_date, open_time, close_time, is_closed, reason) VALUES
(1,'2025-12-30','05:00:00','23:00:00',0,'Special Event Extended'),
(2,'2025-12-30','05:00:00','23:00:00',0,'Special Event Extended'),
(3,'2025-12-30','05:00:00','23:00:00',0,'Special Event Extended'),
(4,'2025-12-30','05:00:00','23:00:00',0,'Special Event Extended'),
(5,'2025-12-30','05:00:00','23:00:00',0,'Special Event Extended');
```

---

# **4. ITEMS (SHOP IDs 1–5)**  
I replaced category IDs with subqueries for accuracy.

### **Shop 1 – Tim Hortons**
```sql
INSERT INTO items (shop_id, name, base_price, description, category_id, availability) VALUES
(1,'Double Double Coffee',2.49,'Medium coffee with 2 cream, 2 sugar',(SELECT category_id FROM item_categories WHERE category_name='Food & Beverages'),'in_stock'),
(1,'Boston Cream Donut',1.29,'Classic donut with vanilla cream filling',(SELECT category_id FROM item_categories WHERE category_name='Food & Beverages'),'in_stock'),
(1,'Chicken Wrap',6.99,'Grilled chicken wrap with vegetables',(SELECT category_id FROM item_categories WHERE category_name='Food & Beverages'),'in_stock'),
(1,'Iced Capp',3.99,'Frozen coffee beverage',(SELECT category_id FROM item_categories WHERE category_name='Food & Beverages'),'in_stock'),
(1,'Bagel with Cream Cheese',2.99,'Fresh bagel with cream cheese',(SELECT category_id FROM item_categories WHERE category_name='Food & Beverages'),'in_stock'),
(1,'Chocolate Chip Cookie',1.49,'Fresh baked chocolate chip cookie',(SELECT category_id FROM item_categories WHERE category_name='Food & Beverages'),'in_stock');
```

### **Shop 2 – Duty Free Shop**
```sql
INSERT INTO items (shop_id, name, base_price, description, category_id, availability) VALUES
(2,'Canadian Maple Syrup',24.99,'Premium 500ml maple syrup',(SELECT category_id FROM item_categories WHERE category_name='Souvenirs & Gifts'),'in_stock'),
(2,'Ice Wine',45.99,'375ml bottle of Canadian ice wine',(SELECT category_id FROM item_categories WHERE category_name='Souvenirs & Gifts'),'in_stock'),
(2,'Maple Leaf Chocolate Box',12.99,'Assorted chocolate box',(SELECT category_id FROM item_categories WHERE category_name='Souvenirs & Gifts'),'in_stock'),
(2,'Perfume Set',89.99,'Luxury perfume gift set',(SELECT category_id FROM item_categories WHERE category_name='Souvenirs & Gifts'),'in_stock'),
(2,'Canadian Whisky',35.99,'750ml bottle of premium whisky',(SELECT category_id FROM item_categories WHERE category_name='Souvenirs & Gifts'),'in_stock'),
(2,'Beaver Plush Toy',15.99,'Cuddly beaver mascot toy',(SELECT category_id FROM item_categories WHERE category_name='Souvenirs & Gifts'),'in_stock');
```

### **Shop 3 – Tech Stop**
```sql
INSERT INTO items (shop_id, name, base_price, description, category_id, availability) VALUES
(3,'USB-C Charging Cable',19.99,'6ft USB-C cable',(SELECT category_id FROM item_categories WHERE category_name='Electronics'),'in_stock'),
(3,'Wireless Earbuds',79.99,'Bluetooth wireless earbuds',(SELECT category_id FROM item_categories WHERE category_name='Electronics'),'in_stock'),
(3,'Travel Adapter',24.99,'Universal travel adapter',(SELECT category_id FROM item_categories WHERE category_name='Electronics'),'in_stock'),
(3,'Portable Power Bank',39.99,'10000mAh power bank',(SELECT category_id FROM item_categories WHERE category_name='Electronics'),'in_stock'),
(3,'Phone Case',29.99,'Protective phone case',(SELECT category_id FROM item_categories WHERE category_name='Electronics'),'in_stock'),
(3,'Screen Protector',14.99,'Tempered glass screen protector',(SELECT category_id FROM item_categories WHERE category_name='Electronics'),'in_stock');
```

### **Shop 4 – Hudson News**
```sql
INSERT INTO items (shop_id, name, base_price, description, category_id, availability) VALUES
(4,'Best Seller Novel',16.99,'Latest bestseller paperback',(SELECT category_id FROM item_categories WHERE category_name='Books & Magazines'),'in_stock'),
(4,'Travel Magazine',5.99,'Monthly travel magazine',(SELECT category_id FROM item_categories WHERE category_name='Books & Magazines'),'in_stock'),
(4,'Crossword Puzzle Book',8.99,'Puzzle book for travel',(SELECT category_id FROM item_categories WHERE category_name='Books & Magazines'),'in_stock'),
(4,'Newspaper',2.99,'Daily newspaper',(SELECT category_id FROM item_categories WHERE category_name='Books & Magazines'),'in_stock'),
(4,'Travel Guide Book',19.99,'Destination travel guide',(SELECT category_id FROM item_categories WHERE category_name='Books & Magazines'),'in_stock'),
(4,'Notebook & Pen Set',12.99,'Journal and pen set',(SELECT category_id FROM item_categories WHERE category_name='Books & Magazines'),'in_stock');
```

### **Shop 5 – The Body Shop**
```sql
INSERT INTO items (shop_id, name, base_price, description, category_id, availability) VALUES
(5,'Hand Cream',12.99,'Moisturizing hand cream',(SELECT category_id FROM item_categories WHERE category_name='Health & Beauty'),'in_stock'),
(5,'Face Cleanser',18.99,'Gentle facial cleanser',(SELECT category_id FROM item_categories WHERE category_name='Health & Beauty'),'in_stock'),
(5,'Lip Balm',6.99,'Hydrating lip balm',(SELECT category_id FROM item_categories WHERE category_name='Health & Beauty'),'in_stock'),
(5,'Body Lotion',15.99,'Nourishing body lotion',(SELECT category_id FROM item_categories WHERE category_name='Health & Beauty'),'in_stock'),
(5,'Travel Size Kit',24.99,'Travel essentials kit',(SELECT category_id FROM item_categories WHERE category_name='Health & Beauty'),'in_stock'),
(5,'Shampoo & Conditioner',16.99,'Hair care duo',(SELECT category_id FROM item_categories WHERE category_name='Health & Beauty'),'in_stock');
```

---

# **5. ITEM VARIANTS (Coffee Sizes)**  
Assuming "Double Double Coffee" exists:

```sql
INSERT INTO item_variants (item_id, variant_type, variant_value, price_adjustment)
SELECT item_id, 'Size', 'Small', 0.00
FROM items WHERE name='Double Double Coffee';

INSERT INTO item_variants (item_id, variant_type, variant_value, price_adjustment)
SELECT item_id, 'Size', 'Medium', 0.00
FROM items WHERE name='Double Double Coffee';

INSERT INTO item_variants (item_id, variant_type, variant_value, price_adjustment)
SELECT item_id, 'Size', 'Large', 0.50
FROM items WHERE name='Double Double Coffee';

INSERT INTO item_variants (item_id, variant_type, variant_value, price_adjustment)
SELECT item_id, 'Size', 'Extra Large', 1.00
FROM items WHERE name='Double Double Coffee';
```

---

# If you want a **single combined SQL file**, I can generate the full `.sql` dump ready to import.

---

