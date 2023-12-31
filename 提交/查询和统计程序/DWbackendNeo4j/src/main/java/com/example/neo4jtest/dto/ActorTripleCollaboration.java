package com.example.neo4jtest.dto;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ActorTripleCollaboration {
    private String actorName1;
    private String actorName2;
    private String actorName3;
    private int totalReviews;

}
