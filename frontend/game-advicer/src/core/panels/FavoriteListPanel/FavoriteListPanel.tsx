import { Panel, List, Cell } from '@vkontakte/vkui'
import React from 'react'
import { PanelBaseProps } from '..'
import {PanelHeader} from "@vkontakte/vkui";

export const FavoriteListPanel: React.FC<PanelBaseProps> = React.memo(
    ({ id }) => {
        return (
            <Panel id={id}>
                <PanelHeader>Список понравившихся</PanelHeader>
                <List>
                    <Cell>Game 1</Cell>
                    <Cell>Game 2</Cell>
                    <Cell>Game 3</Cell>
                </List>
            </Panel>
        )
    }
)
