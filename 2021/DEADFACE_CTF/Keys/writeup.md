# Writeup

`loans`テーブルから外部キーを見つければよい。

```sql
DROP TABLE IF EXISTS `loans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loans` (
  `loan_id` smallint NOT NULL AUTO_INCREMENT,
  `cust_id` smallint NOT NULL,
  `employee_id` smallint NOT NULL,
  `amt` decimal(10,2) NOT NULL,
  `balance` decimal(10,2) NOT NULL,
  `interest` decimal(10,2) DEFAULT NULL,
  `loan_type_id` smallint NOT NULL,
  PRIMARY KEY (`loan_id`),
  KEY `fk_loans_cust_id` (`cust_id`),
  KEY `fk_loans_employee_id` (`employee_id`),
  KEY `fk_loans_loan_type_id` (`loan_type_id`),
  CONSTRAINT `fk_loans_cust_id` FOREIGN KEY (`cust_id`) REFERENCES `customers` (`cust_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_loans_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_loans_loan_type_id` FOREIGN KEY (`loan_type_id`) REFERENCES `loan_types` (`loan_type_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1785 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
```

以下が外部キーである。

```sql
`fk_loans_cust_id`
`fk_loans_employee_id`
`fk_loans_loan_type_id`
```

<!-- flag{fk_loans_cust_id} -->
