import Cell from '@vkontakte/vkui/dist/components/Cell/Cell';
import List from '@vkontakte/vkui/dist/components/List/List';
import Panel from '@vkontakte/vkui/dist/components/Panel/Panel';
import React from 'react';
import {PanelBaseProps} from "..";

export const FavoriteListPanel:React.FC<PanelBaseProps> = React.memo(({id}) => {
    return (
        <Panel id={id}>
            <List>
                <Cell>Game 1</Cell>
                <Cell>Game 2</Cell>
                <Cell>Game 3</Cell>
            </List>
        </Panel>
    );
});
