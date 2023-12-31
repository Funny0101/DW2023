package com.mysql.dwbackened.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.mysql.dwbackened.dto.MovieSearchDto;
import com.mysql.dwbackened.entity.ReviewSentiment;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.Collection;
import java.util.List;
import java.util.Set;

/**
 * @author wyx20
 * @version 1.0
 * @title ReviewMapper
 * @description
 * @create 2023/12/30 20:42
 */
@Mapper
public interface ReviewMapper extends BaseMapper<ReviewSentiment> {

    @Select("SELECT DISTINCT movie_id " +
            "FROM movie " +
            "WHERE review_sentiment_rate >= #{positive}")
    Set<String> selectByPositive(float positive);

    @Select("SELECT " +
            "     review_sentiment_rate " +
            " FROM " +
            "    movie " +
            "WHERE" +
            "    movie_id = #{movieId} ")
    float selectPositiveByMovieId(String movieId);

//    @Select("SELECT " +
//            " COALESCE(SUM(CASE WHEN sentiment_score >= 0.2 THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0), 0) " +
//            " FROM " +
//            " review_sentiment " +
//            "WHERE" +
//            " movie_id = concat(#{movieId},'\n')")
}
