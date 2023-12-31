package com.example.neo4jtest.entity;

import org.springframework.data.neo4j.core.schema.Id;
import org.springframework.data.neo4j.core.schema.Node;

@Node
public class Director {
    @Id
    private Integer directorId;
    private String directorName;

    // 构造函数
    public Director() {}

    public Director(Integer directorId, String directorName) {
        this.directorId = directorId;
        this.directorName = directorName;
    }

    // Getter和Setter
    public Integer getDirectorId() {
        return directorId;
    }

    public void setDirectorId(Integer directorId) {
        this.directorId = directorId;
    }

    public String getDirectorName() {
        return directorName;
    }

    public void setDirectorName(String directorName) {
        this.directorName = directorName;
    }
}
