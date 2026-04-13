# Odoo CRM / Order Management Module

## 📌 项目介绍
本项目基于 Odoo 17 开发，实现一个简化的订单管理系统，包含客户管理、订单管理及订单明细功能，模拟企业实际ERP业务流程。

---

## 🧱 技术栈
- Python
- Odoo 17
- PostgreSQL
- XML（Odoo View）

---

## 🚀 核心功能

### 1️⃣ 订单管理
- 创建、编辑订单
- 自动生成订单编号（Sequence）
- 金额自动计算
- 订单状态流转：
  - 草稿（Draft）
  - 已确认（Confirmed）
  - 已完成（Done）
- API接口

## API示例
POST /api/orders  
POST /api/create_order

---

### 2️⃣ 客户关联
- 使用 Many2one 将订单关联到客户（res.partner）
- 在客户页面中展示相关订单（One2many）

---

### 3️⃣ 订单明细
- 支持多条订单行（One2many）
- 每条明细包含：
  - 产品名称
  - 数量
  - 单价
  - 小计自动计算

---

### 4️⃣ 金额计算
- 使用 `@api.depends` 自动计算订单总金额
- 实现业务数据实时更新

---

### 5️⃣ 业务逻辑控制
- 订单必须包含明细才能确认
- 使用 `UserError` 提示非法操作
- 状态按钮控制业务流程

---

## 🧠 技术要点

- 使用 Odoo ORM 定义模型
- 使用 One2many / Many2one 建立数据关系
- 使用 compute 实现动态字段计算
- 重写 create 方法实现订单编号自动生成
- 使用 XML 定义 Tree / Form 视图
- 使用按钮调用 Python 方法实现业务逻辑

---

## 📂 项目结构
my_addons/
└── my_crm/
├── models/
├── views/
├── data/
└── manifest.py

---

## ⚙️ 使用方法

1. 启动 Odoo 17
2. 将模块放入 `addons_path`
3. 更新模块：python3 odoo-bin -u my_crm
   
---

## 📈 项目收获

通过该项目掌握：
- Odoo模块开发流程
- ERP系统基本业务逻辑
- Python在企业系统中的应用

- ## 📷 系统截图

### 订单列表
![list](screenshots/list.png)

### 订单详情
![form](screenshots/form.png)
