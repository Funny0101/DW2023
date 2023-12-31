package com.mysql.dwbackened.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author wyx20
 * @version 1.0
 * @title Actor
 * @description
 * @create 2023/12/25 13:42
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Actor {
    @TableId(type = IdType.AUTO)
    private Integer actorId;
    private String actorName;
}
