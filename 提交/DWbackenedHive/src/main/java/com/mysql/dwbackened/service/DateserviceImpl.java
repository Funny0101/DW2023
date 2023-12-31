package com.mysql.dwbackened.service;

import com.mysql.dwbackened.mapper.DateMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;

/**
 * @author wyx20
 * @version 1.0
 * @title DateserviceImpl
 * @description
 * @create 2023/12/25 8:54
 */
@Service
public class DateserviceImpl implements DateService{
    @Autowired
    private DateMapper dateMapper;
    @Override
    public HashMap<String,Object> findByYear(String year) {
        HashMap<String,Object> result=new HashMap<>();

        result.put("num",dateMapper.selectByYear(year));
//        result.put("data",);
        return result;
    }
}
