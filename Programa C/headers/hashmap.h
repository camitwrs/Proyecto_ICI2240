//
//  HashMap.h
//  TablaHashLab
//
//  Created by Matias Barrientos on 11-08-18.
//  Copyright © 2018 Matias Barrientos. All rights reserved.
//

#ifndef HashMap_h
#define HashMap_h


typedef struct HashMap HashMap;

typedef struct HashMapPair {
     char * key;
     void * value;
} HashMapPair;

HashMap * createMap(long capacity);

void insertMap(HashMap * table, char * key, void * value);

void eraseMap(HashMap * table, char * key);

HashMapPair * searchMap(HashMap * table, char * key);

HashMapPair * firstMap(HashMap * table);

HashMapPair * nextMap(HashMap * table);

void enlarge(HashMap * map);

#endif /* HashMap_h */