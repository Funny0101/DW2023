package com.example.neo4jtest.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.neo4j.core.schema.Node;

import java.io.Serializable;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class ActorDirectorCollaboration implements Serializable {
    private static final long serialVersionUID = 1L; // 可选，但推荐

    private String actorName;
    private String directorName;
    private int collaborationCount;
}
