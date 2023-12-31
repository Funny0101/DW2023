package com.mysql.dwbackened.service;

import java.util.HashMap;

/**
 * @author wyx20
 * @version 1.0
 * @title DateService
 * @description
 * @create 2023/12/25 8:50
 */
public interface DateService {
    HashMap<String,Object> findByYear(String year);
}
