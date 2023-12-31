package com.example.neo4jtest.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ActorDoubleCollaboration {
    private String actorName1;
    private String actorName2;
    private int totalReviews;

}
