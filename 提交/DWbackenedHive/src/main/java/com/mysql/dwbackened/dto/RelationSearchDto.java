package com.mysql.dwbackened.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author wyx20
 * @version 1.0
 * @title RelationSearchDto
 * @description
 * @create 2023/12/26 21:11
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class RelationSearchDto {
    private String source;
    private int page;
    private int per_page;
}
