package com.example.neo4jtest.entity;

import org.springframework.data.neo4j.core.schema.Id;
import org.springframework.data.neo4j.core.schema.Node;

@Node
public class Movie {
    @Id
    private String movieId;
    private String movieTitle;
    private String movieGenre;
    private Integer movieReviewNum;

    // 构造函数
    public Movie() {}

    public Movie(String movieId, String movieTitle, String movieGenre, Integer movieReviewNum) {
        this.movieId = movieId;
        this.movieTitle = movieTitle;
        this.movieGenre = movieGenre;
        this.movieReviewNum = movieReviewNum;
    }

    // Getter和Setter
    public String getMovieId() {
        return movieId;
    }

    public void setMovieId(String movieId) {
        this.movieId = movieId;
    }

    public String getMovieTitle() {
        return movieTitle;
    }

    public void setMovieTitle(String movieTitle) {
        this.movieTitle = movieTitle;
    }

    public String getMovieGenre() {
        return movieGenre;
    }

    public void setMovieGenre(String movieGenre) {
        this.movieGenre = movieGenre;
    }

    public Integer getMovieReviewNum() {
        return movieReviewNum;
    }

    public void setMovieReviewNum(Integer movieReviewNum) {
        this.movieReviewNum = movieReviewNum;
    }
}
